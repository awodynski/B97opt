import numpy as np
from typing import Any, Dict, List
from ACONF import ACONF
from ADIM6 import ADIM6
from AHB21 import AHB21
from AL2X6 import AL2X6
from ALK8 import ALK8
from ALKBDE10 import ALKBDE10
from AMINO20x4 import AMINO20x4
from BH76 import BH76
from BH76RC import BH76RC
from BHDIV10 import BHDIV10
from BHPERI import BHPERI
from BHROT27 import BHROT27
from BSR36 import BSR36
from BUT14DIOL import BUT14DIOL
from C60ISO import C60ISO
from CARBHB12 import CARBHB12
from CDIE20 import CDIE20
from CHB6 import CHB6
from DARC import DARC
from DC13 import DC13
from DIPCS10 import DIPCS10
from FH51 import FH51
from G21EA import G21EA
from G21IP import G21IP
from G2RC import G2RC
from HAL59 import HAL59
from HEAVY28 import HEAVY28
from HEAVYSB11 import HEAVYSB11
from ICONF import ICONF
from IDISP import IDISP
from IL16 import IL16
from INV24 import INV24
from ISO34 import ISO34
from ISOL24 import ISOL24
from MB1643 import MB1643
from MCONF import MCONF
from NBPRC import NBPRC
from PA26 import PA26
from PArel import PArel
from PCONF21 import PCONF21
from PNICO23 import PNICO23
from PX13 import PX13
from RC21 import RC21
from RG18 import RG18
from RSE43 import RSE43
from S22 import S22
from S66 import S66
from SCONF import SCONF
from SIE4x4 import SIE4x4
from TAUT15 import TAUT15
from UPU23 import UPU23
from W411 import W411
from WATER27 import WATER27
from WCPT18 import WCPT18
from YBDE18 import YBDE18
from W417 import W417


def read_data(file_name: str,
              testsets_dict: Dict[str, Any],
              L2_B97: float,
              a1: float,
              a2: float,
              Nsplit: int,
              seed: int,
              select_split: int,
              base_path: str,
              dftd4_path: str,
              MP2: bool = False) -> Dict[str, Any]:
    """
    Reads data from the given file and constructs a data_all dictionary.
    Assumes LMF dimension is fixed to 1 (no centroids).

    Parameters:
        file_name (str): Name of the file to read.
        testsets_dict (Dict[str, Any]): Dictionary with test set info.
        L2_B97 (float): Regularization weight for B97.
        a1 (float): Parameter a1 for dispersion energies.
        a2 (float): Parameter a2 for dispersion energies.
        Nsplit (int): Number of splits for random assignment.
        seed (int): Seed for random number generator.
        select_split (int): Selector for the split.
        base_path (str): Base path to the test set library.
        dftd4_path (str): Path to the dftd4 executable.
        MP2 (bool, optional): Flag indicating use of MP2 terms.

    Returns:
        Dict[str, Any]: A dictionary with the data and related parameters.
    """
    data: Dict[str, Dict[str, Any]] = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            main_key = parts[0]
            sub_key = parts[1]
            values = np.array(list(map(float, parts[2:])))
            if main_key not in data:
                data[main_key] = {}
            if MP2:
                data[main_key][sub_key] = {
                    'E_1e': values[0],
                    'E_xx': values[1],
                    'E_1_del': values[2],
                    'E_lmf_del': values[3:4],
                    'Ec_opp': values[4:10],
                    'Ec_ss': values[10:17],
                    'E_mp2': values[601:603]
                }
            else:
                data[main_key][sub_key] = {
                    'E_1e': values[0],
                    'E_xx': values[1],
                    'E_1_del': values[2],
                    'E_lmf_del': values[3:4],
                    'Ec_opp': values[4:10],
                    'Ec_ss': values[10:17]
                }
    testsets = _testset(testsets_dict, a1, a2, Nsplit, seed,
                        base_path, dftd4_path)
    data_all = {
        'data': data,
        'testsets': testsets,
        'testsets_dict': testsets_dict,
        'L2_B97': L2_B97,
        'select_split': select_split,
        'MP2': MP2,
        'base_path': base_path,
        'dftd4_path': dftd4_path
    }
    return data_all


def _select_class(klasa: str) -> Any:
    """
    Returns an instance of the class corresponding to the provided key.

    Parameters:
        klasa (str): Key representing the desired class.

    Returns:
        Any: An instance of the selected class.
    """
    available_classes = {
        "ACONF": ACONF,
        "ADIM6": ADIM6,
        "AHB21": AHB21,
        "AL2X6": AL2X6,
        "ALK8": ALK8,
        "ALKBDE10": ALKBDE10,
        "AMINO20x4": AMINO20x4,
        "BH76": BH76,
        "BH76RC": BH76RC,
        "BHDIV10": BHDIV10,
        "BHPERI": BHPERI,
        "BHROT27": BHROT27,
        "BSR36": BSR36,
        "BUT14DIOL": BUT14DIOL,
        "C60ISO": C60ISO,
        "CARBHB12": CARBHB12,
        "CDIE20": CDIE20,
        "CHB6": CHB6,
        "DARC": DARC,
        "DC13": DC13,
        "DIPCS10": DIPCS10,
        "FH51": FH51,
        "G21EA": G21EA,
        "G21IP": G21IP,
        "G2RC": G2RC,
        "HAL59": HAL59,
        "HEAVY28": HEAVY28,
        "HEAVYSB11": HEAVYSB11,
        "ICONF": ICONF,
        "IDISP": IDISP,
        "IL16": IL16,
        "INV24": INV24,
        "ISO34": ISO34,
        "ISOL24": ISOL24,
        "MB1643": MB1643,
        "MCONF": MCONF,
        "NBPRC": NBPRC,
        "PA26": PA26,
        "PArel": PArel,
        "PCONF21": PCONF21,
        "PNICO23": PNICO23,
        "PX13": PX13,
        "RC21": RC21,
        "RG18": RG18,
        "RSE43": RSE43,
        "S22": S22,
        "S66": S66,
        "SCONF": SCONF,
        "SIE4x4": SIE4x4,
        "TAUT15": TAUT15,
        "UPU23": UPU23,
        "W411": W411,
        "WATER27": WATER27,
        "WCPT18": WCPT18,
        "YBDE18": YBDE18,
        "W417": W417,
    }
    return available_classes[klasa]()


def _testset(testsets_dict: Dict[str, Any],
             a1: float,
             a2: float,
             Nsplit: int,
             seed: int,
             base_path: str,
             dftd4_path: str) -> Dict[str, Any]:
    """
    Prepares testset instances by initializing and processing each test set.
    Assigns the base_path and dftd4_path to each instance.

    Parameters:
        testsets_dict (Dict[str, Any]): Dictionary with test set info.
        a1 (float): Parameter a1 for dispersion energy calculation.
        a2 (float): Parameter a2 for dispersion energy calculation.
        Nsplit (int): Number of splits for random assignment.
        seed (int): Seed for random number generator.
        base_path (str): Base path to the test set library.
        dftd4_path (str): Path to the dftd4 executable.

    Returns:
        Dict[str, Any]: A dictionary of testset instances.
    """
    testsets: Dict[str, Any] = {}
    for testset_name, _ in testsets_dict.items():
        instance = _select_class(testset_name)
        instance.base_path = base_path
        instance.dftd4_path = dftd4_path
        instance.calculate_dispersion_energies(testset_name, a1, a2)
        instance.assign_random_values(Nsplit, seed)
        testsets[testset_name] = instance
    return testsets

