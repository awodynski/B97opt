import numpy as np
import math
import subprocess
import ast
import tensorflow as tf
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Tuple, Optional


def _update_parameters(together_params: Any,
                       optimize_indices: List[int],
                       params: List[float]) -> tf.Tensor:
    """
    Updates the parameter tensor by replacing specified indices with
    new parameter values.

    Parameters:
        together_params (Any): The full parameter tensor or array.
        optimize_indices (List[int]): Indices of parameters to update.
        params (List[float]): New parameter values to insert.

    Returns:
        tf.Tensor: Updated parameter tensor.
    """
    optimize_indices_tensor = tf.constant(optimize_indices, dtype=tf.int32)
    together_params_tensor = tf.convert_to_tensor(
        together_params, dtype=tf.float64)
    updates = tf.convert_to_tensor(params, dtype=tf.float64)
    scatter_indices = tf.expand_dims(optimize_indices_tensor, axis=1)
    updated_params = tf.tensor_scatter_nd_update(
        together_params_tensor, scatter_indices, updates)
    return updated_params


def _calculate_energy(data: Dict[str, Any],
                      testset: str,
                      molecule: str,
                      scal_lmf: tf.Tensor,
                      scal_opp: tf.Tensor,
                      scal_ss: tf.Tensor,
                      scal_mp2: Optional[tf.Tensor] = None,
                      MP2_flag: bool = False) -> tf.Tensor:
    """
    Computes the total energy for a given molecule using provided scaling factors.

    Parameters:
        data (Dict[str, Any]): Dictionary containing energy components for
            each molecule.
        testset (str): Identifier for the test set.
        molecule (str): Identifier for the molecule.
        scal_lmf (tf.Tensor): Tensor for LMF scaling factor.
        scal_opp (tf.Tensor): Tensor for opposite-spin scaling factors.
        scal_ss (tf.Tensor): Tensor for same-spin scaling factors.
        scal_mp2 (Optional[tf.Tensor]): Tensor for MP2 scaling factors, required
            if MP2_flag is True.
        MP2_flag (bool): Flag indicating whether MP2 energy contributions
            should be included.

    Returns:
        tf.Tensor: Computed total energy for the molecule.
    """
    E_1e = tf.constant(data[testset][molecule]['E_1e'], dtype=tf.float64)
    E_xx = tf.constant(data[testset][molecule]['E_xx'], dtype=tf.float64)
    E_1_del = tf.constant(data[testset][molecule]['E_1_del'], dtype=tf.float64)
    E_lmf_del = tf.constant(data[testset][molecule]['E_lmf_del'], dtype=tf.float64)
    Ec_opp = tf.constant(data[testset][molecule]['Ec_opp'], dtype=tf.float64)
    Ec_ss = tf.constant(data[testset][molecule]['Ec_ss'], dtype=tf.float64)
#AW do we need that?
    #scal_lmf = tf.convert_to_tensor(scal_lmf, dtype=tf.float64)
    #scal_opp = tf.convert_to_tensor(scal_opp, dtype=tf.float64)
    #scal_ss = tf.convert_to_tensor(scal_ss, dtype=tf.float64)

    bc97 = (tf.reduce_sum(scal_opp * Ec_opp) +
            tf.reduce_sum(scal_ss * Ec_ss))
    lmf_del = tf.reduce_sum(scal_lmf * E_lmf_del)

    if MP2_flag:
        #scal_mp2 = tf.convert_to_tensor(scal_mp2, dtype=tf.float64)
        E_mp2 = tf.constant(data[testset][molecule]['E_mp2'], dtype=tf.float64)
        mp2 = tf.reduce_sum(scal_mp2 * E_mp2)
        E_tot = E_1e + E_xx + E_1_del - lmf_del + bc97 + mp2
    else:
        E_tot = E_1e + E_xx + E_1_del - lmf_del + bc97

    return E_tot


def _string_to_expression(s: str,
                          var_dict: Dict[str, tf.Tensor]) -> tf.Tensor:
    """
    Evaluates a mathematical expression provided as a string using
    TensorFlow.

    The function replaces variable placeholders in the expression with
    their corresponding values from the provided dictionary and then
    evaluates the expression using eval().

    Parameters:
        s (str): The string representation of the mathematical
            expression.
        var_dict (Dict[str, tf.Tensor]): Dictionary mapping variable names
            to TensorFlow tensors.

    Returns:
        tf.Tensor: Evaluated expression as a TensorFlow tensor.
    """
    for var_name, value in var_dict.items():
        s = s.replace(f"['{var_name}']",
                      f"var_dict['{var_name}']")
    return tf.convert_to_tensor(eval(s))


def loss_function(data_all: Dict[str, Any],
                  params: List[float], together_params: Any,
                  optimize_indices: List[int]
                  ) -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor,
                             Dict[str, tf.Tensor]]:
    """
    Computes the scaled loss value for the given parameters.

    This function updates the parameters to be optimized within a combined
    parameter tensor, calculates various energy components for a set of
    molecules, and computes a scaled loss value based on weighted Mean
    Absolute Errors (MAEs) for training, validation, and combined test sets.
    The LMF scaling factor is fixed to a dimension of 1.

    Parameters:
        data_all (Dict[str, Any]): Dictionary containing test set data
            and metadata.
        params (List[float]): List of parameters to optimize.
        together_params (Any): Combined parameter array/tensor.
        optimize_indices (List[int]): Indices in together_params to be
            updated.

    Returns:
        Tuple containing:
            - scaled_loss (tf.Tensor): Final scaled loss value.
            - scaled_loss_1 (tf.Tensor): Weighted MAE for training split.
            - scaled_loss_2 (tf.Tensor): Weighted MAE for validation split.
            - scaled_loss_3 (tf.Tensor): Weighted MAE for combined test sets.
            - all_loss (Dict[str, tf.Tensor]): Dictionary of individual loss
              components.
    """
    updated_params = _update_parameters(together_params, optimize_indices,
                                        params)

    MP2_flag = data_all['MP2']
    LMF_dim = 1  # Fixed dimension for LMF scaling factor.
    scal_lmf = updated_params[0:LMF_dim]
    scal_opp = updated_params[LMF_dim:LMF_dim + 6]
    scal_ss = updated_params[LMF_dim + 6:LMF_dim + 13]
    scal_disp = updated_params[LMF_dim + 13:LMF_dim + 15]
    if MP2_flag:
        scal_mp2 = updated_params[LMF_dim + 15:LMF_dim + 17]
    else:
        scal_mp2 = None

    l2_norm_b97 = (tf.norm(scal_opp[1:6], ord=2) +
                   tf.norm(scal_ss[1:7], ord=2))

    efull: Dict[str, Dict[str, tf.Tensor]] = {}
    for testset, _ in data_all['testsets_dict'].items():
        efull[testset] = {}
        for molecule in data_all['testsets'][testset].molecules:
            energy = _calculate_energy(data_all['data'], testset, molecule,
                                       scal_lmf, scal_opp, scal_ss,
                                       scal_mp2, MP2_flag)
            disp_energy = (data_all['testsets'][testset]
                           .dispersion_energy_results[molecule]['s6'] *
                           scal_disp[0] +
                           data_all['testsets'][testset]
                           .dispersion_energy_results[molecule]['s8'] *
                           scal_disp[1] +
                           data_all['testsets'][testset]
                           .dispersion_energy_results[molecule]['s9'])
            efull[testset][molecule] = energy + disp_energy

    scaled_loss = 0.0
    scaled_loss_1 = 0.0
    scaled_loss_2 = 0.0
    wtmad_2_train = 0.0
    wtmad_2_validate = 0.0
    wtmad_2_together = 0.0
    mae_train: Dict[str, float] = {}
    mae_validate: Dict[str, float] = {}
    mae_together: Dict[str, float] = {}

    for testset, weight in data_all['testsets_dict'].items():
        mae_train[testset] = 0.0
        mae_validate[testset] = 0.0
        mae_together[testset] = 0.0
        energy_results: Dict[str, tf.Tensor] = {}
        num_zeros = sum(1 for v in data_all['testsets']
                        [testset].random_split.values() if v == 0)
        num_ones = sum(1 for v in data_all['testsets']
                       [testset].random_split.values() if v == 1)
        for key, expr in data_all['testsets'][testset] \
                           .testset_calculations.items():
            energy_results[key] = _string_to_expression(expr,
                                                          efull[testset])
            conversion_factor = 627.5096080305927
            tmp = abs(energy_results[key] * conversion_factor -
                      data_all['testsets'][testset].exp_values[key])
            mae_train[testset] += (tmp / num_ones *
                                   data_all['testsets'][testset]
                                   .random_split[key])
            mae_validate[testset] += (tmp / num_zeros *
                                      (1 - data_all['testsets']
                                       [testset].random_split[key]))
            mae_together[testset] += (tmp /
                                      len(data_all['testsets']
                                          [testset]
                                          .testset_calculations))
        wtmad_2_train += mae_train[testset] * weight
        wtmad_2_validate += mae_validate[testset] * weight
        wtmad_2_together += mae_together[testset] * weight

    if data_all['select_split'] == 0:
        scaled_loss = wtmad_2_train
        scaled_loss_1 = wtmad_2_train
        scaled_loss_2 = wtmad_2_validate
    elif data_all['select_split'] == 1:
        scaled_loss = wtmad_2_validate
        scaled_loss_1 = wtmad_2_validate
        scaled_loss_2 = wtmad_2_train
    else:
        scaled_loss = wtmad_2_together
        scaled_loss_1 = wtmad_2_train
        scaled_loss_2 = wtmad_2_validate

    scaled_loss_3 = wtmad_2_together
    scaled_loss = (scaled_loss +
                   l2_norm_b97 * data_all['L2_B97'])

    all_loss = {
        'wtmad_2_train': scaled_loss_1,
        'L2_B97': l2_norm_b97
    }

    return (scaled_loss, scaled_loss_1, scaled_loss_2,
            scaled_loss_3, all_loss)

