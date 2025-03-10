import sys
sys.path.insert(0, '../new/')
import numpy as np
import tensorflow as tf
from read_data import read_data 
from multistart_optimizer import multistart_optimization_parallel

L2_B97 = 0.00

TESTSETS = {
    "ACONF": 0.309569196,  
    "ADIM6": 0.06744186,
    "AHB21": 0.035265286,
    "AL2X6": 0.006315626,
    "ALK8": 0.00482651,
    "ALKBDE10": 0.003750863,
    "AMINO20x4": 1.238276782,
    "BH76": 0.154235657,
    "BH76RC": 0.052969764,
    "BHDIV10": 0.008331666,
    "BHPERI": 0.047050958,
    "BHROT27": 0.162634917,
    "BSR36": 0.083927649,
    "BUT14DIOL": 0.863255814,
    "C60ISO": 0.003459613,
    "CARBHB12": 0.075034653,
    "CDIE20": 0.186046512,
    "CHB6": 0.008458554,
    "DARC": 0.016284083,
    "DC13": 0.008930097,
    "DIPCS10": 0.000577254,
    "FH51": 0.062113497,
    "G21EA": 0.028084058,
    "G21IP": 0.005277854,
    "G2RC": 0.018419548,
    "HAL59": 0.48546385,
    "HEAVY28": 0.852813203,
    "HEAVYSB11": 0.007160322,
    "ICONF": 0.196344499,
    "IDISP": 0.015935629,
    "IL16": 0.005541811,
    "INV24": 0.028458983,
    "ISO34": 0.088132671,
    "ISOL24": 0.041351214,
    "MB1643": 0.003915801,
    "MCONF": 0.387553226,
    "NBPRC": 0.016355442,
    "PA26": 0.005194147,
    "PArel": 0.163142297,
    "PCONF21": 0.419638243,
    "PNICO23": 0.203431186,
    "PX13": 0.014717528,
    "RC21": 0.022216142,
    "RG18": 1.172093023,
    "RSE43": 0.213684211,
    "S22": 0.113819688,
    "S66": 0.455694911,
    "SCONF": 0.139575329,
    "SIE4x4": 0.017920494,
    "TAUT15": 0.185741517,
    "UPU23": 0.151862091,
    "W411": 0.017227988,
    "WATER27": 0.012567426,
    "WCPT18": 0.019428807,
    "YBDE18": 0.013794926
}

BASE_PATH = './GMTKN55'
DFTD4_PATH = '/path/to/dftd4/program/dftd4'

# READ DATA
data_all = read_data(
    file_name='results.out',
    testsets_dict=TESTSETS,
    L2_B97=L2_B97,
    a1=0.8927901705838597,
    a2=3.0193269791202924,
    Nsplit=50,
    seed=42,
    select_split=2,
    base_path=BASE_PATH,
    dftd4_path=DFTD4_PATH,
    MP2=True
)

# INITIAL PARAMETERS
INITIAL_PARAMS = np.zeros(18)
OPTIMIZE_INDICES = list(range(18))
BOUNDS = tuple((0, 1.5) for _ in range(18))

# MULTISTART OPTIMIZATION
# Note: The multistart_optimization_parallel function now creates the cache internally.
best_results = multistart_optimization_parallel(
    data_all=data_all,
    initial_params=INITIAL_PARAMS,
    optimize_indices=OPTIMIZE_INDICES,
    bounds=BOUNDS,
    N=30,
    min_dist=0.1
)

print("Best parameters:", best_results.x)
print("Best loss value:", best_results.fun)

