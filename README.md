# B97 and D4 Linear Parameter Optimizatior

This project implements a multistart optimization framework for computational chemistry applications. The program optimizes linear parameters for the B97 functional against GMTKN55 and integrates external dispersion energy calculations via the DFTD4 program. It reads test set data, computes loss and gradient functions using TensorFlow, and uses SciPy's optimization routines to search for the optimal parameters.

## Features

- **Data Processing:**  
  Reads and processes test set data from an input file (e.g., `results.out`).

- **B97 Linear Parameter Optimization:**  
  The program specifically optimizes linear parameters for the B97 functional and D4 correction.

- **Loss Function & Gradient Caching:**  
  Implements a custom loss function with TensorFlow caching for efficient gradient computation.

- **Multistart Optimization:**  
  Uses multistart optimization (via SciPy's `minimize`) to search for the optimal parameters across multiple initial guesses.

- **Dispersion Energy Calculation:**  
  Integrates external dispersion energy calculations via the DFTD4 program, executed using Python's subprocess module.

- **Configurable Paths:**  
  Allows dynamic configuration of the GMTKN55 library path (`BASE_PATH`) and DFTD4 executable path (`DFTD4_PATH`).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/awodynski/B97opt.git
   cd B97opt
   ```

2. **Install Dependencies:**

   Ensure you have Python 3 installed. Then install the required packages:

   ```bash
   pip install numpy tensorflow scipy
   ```

3. **External Programs:**

   Ensure that the DFTD4 program is installed and available at the specified `DFTD4_PATH`. Adjust this path in the main configuration if necessary.

## Usage

1. **Configure Constants:**

   Open the main program file (e.g., `calc.py`) and adjust the following constants as needed:
   
   - **L2_B97:** Regularization weight for the B97 functional.
   - **TESTSETS:** Dictionary containing test set names and corresponding weights.
   - **BASE_PATH:** Path to the test set library (e.g., GMTKN55).
   - **DFTD4_PATH:** Path to the DFTD4 executable.
   - **a1 and a2:** Nonlinear dispersion energy D4 parameters.
   - Other parameters such as the number of random splits, seed, and optimization settings.

2. **Run the Program:**

   Execute the main program:

   ```bash
   python calc.py
   ```

   The program will:
   - Read the input data from `results.out`.
   - Create a cache for loss and gradient computation internally during multistart optimization.
   - Optimize linear parameters for the B97 functional.
   - Print the best parameters and the corresponding loss value.

## Code Structure

- **read_data.py:**  
  Contains the `read_data` function that reads and prepares input data, incorporating dynamic paths for the test set library and DFTD4.

- **loss_and_gradient_cache.py:**  
  Implements loss and gradient computation with TensorFlow caching.

- **multistart_optimizer.py:**  
  Contains the `multistart_optimization_parallel` function that performs multistart optimization and creates the cache.

- **optimization_utils.py:**  
  Provides additional utility functions for the optimization process.

- **TestsetClass (and its variants):**  
  Contains methods for handling test set-specific calculations, including dispersion energy calculations via an internal method `_run_dftd4`.

## Configuration

Main configuration settings include:
- **L2_B97:** Regularization parameter for the B97 functional.
- **TESTSETS:** Test set dictionary with weights (weights are hosen to reproduce WTMAD-2).
- **BASE_PATH & DFTD4_PATH:** Paths for input data and the external DFTD4 executable.
- **INITIAL_PARAMS:** Initial guess for the parameter vector (total size of 18 parameters: LMF scaling, B97opp 6 parameters, B97par 7 parameters, S6 (D4), S8 (D4), MP2opp, MP2par).
- **OPTIMIZE_INDICES & BOUNDS:** Indices to optimize and parameter bounds.
- **MP2 Flag:** Boolean flag indicating whether MP2 energy contributions are used.

## License

This project is licensed under the MIT License.

## Acknowledgements

The code was edited using ChatGPT for clarity and consistency.

