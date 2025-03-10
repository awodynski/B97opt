import tensorflow as tf
from typing import Any, Dict, List, Tuple
from loss_function import loss_function


class LossAndGradientCache:
    """
    A class to cache and compute loss and gradients using TensorFlow.
    """

    def __init__(self, num_params: int, data_all: Dict[str, Any],
                 fixed_params: Any, optimize_indices: List[int]) -> None:
        """
        Initializes the LossAndGradientCache instance.

        Parameters:
            num_params (int): Number of parameters to optimize.
            data_all (Dict[str, Any]): Data for loss computation.
            fixed_params (Any): Fixed parameters not subject to optimization.
            optimize_indices (List[int]): Indices of parameters to optimize.
        """
        self.data_all = data_all
        self.fixed_params = tf.constant(fixed_params, dtype=tf.float64)
        self.optimize_indices = tf.constant(optimize_indices, dtype=tf.int32)
        self.x_tf = tf.Variable(tf.zeros(num_params, dtype=tf.float64),
                                trainable=True)

    @tf.function
    def loss_and_gradient(self, opt_params: tf.Tensor
                         ) -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor,
                                    tf.Tensor, tf.Tensor,
                                    Dict[str, tf.Tensor]]:
        """
        Computes loss and gradient for the given parameters.

        Parameters:
            opt_params (tf.Tensor): Parameters to optimize.

        Returns:
            Tuple: Loss, gradient, and additional loss values.
        """
        self.x_tf.assign(opt_params)
        with tf.GradientTape() as tape:
            tape.watch(self.x_tf)
            loss, loss_1, loss_2, loss_3, all_loss = loss_function(
                self.data_all,  self.x_tf, self.fixed_params,
                self.optimize_indices)
        grad = tape.gradient(loss, self.x_tf)
        return loss, grad, loss_1, loss_2, loss_3, all_loss

