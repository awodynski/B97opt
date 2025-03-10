import random
import subprocess
from typing import Dict, Any, Optional

class TestsetClass:
    """
    A class for handling test sets and calculating dispersion energies.
    """

    def assign_random_values(self, N: int = 50, seed: int = 42) -> None:
        """
        Creates a new dictionary with the same keys as 'testset_calculations',
        where N% of them are assigned a value of 1 and the rest 0.

        Parameters:
            N (int): Percentage of keys selected for training (default is 50). 
            seed (int): Seed for the random number generator (default is 42).
        """
        keys = list(self.testset_calculations.keys())
        random.seed(seed)
        number_of_ones = int(len(keys) * N / 100)
        chosen_keys = random.sample(keys, number_of_ones)
        self.random_split = {k: 1 if k in chosen_keys else 0 for k in keys}

    def _run_dftd4(self, a1: float, a2: float, coord_path: str,
                   molecule_charge: float) -> Optional[Dict[str, float]]:
        """
        Internal method to run the external DFTD4 program and calculate
        dispersion energies.

        Parameters:
            a1 (float): Parameter a1 for DFTD4.
            a2 (float): Parameter a2 for DFTD4.
            coord_path (str): Path to the coordinate file.
            molecule_charge (float): Charge of the molecule.

        Returns:
            Optional[Dict[str, float]]: A dictionary with keys 's6', 's8',
            and 's9' containing the dispersion energies, or None if an error occurs.
        """
        command_s6 = (
            f"{self.dftd4_path} --charge {molecule_charge} --input coord "
            f"--param 1.0 0.0 {a1} {a2} --mbdscale 0.0 --silent {coord_path} | "
            f"grep 'Dispersion energy:' | awk '{{print $3}}'"
        )
        command_s8 = (
            f"{self.dftd4_path} --charge {molecule_charge} --input coord "
            f"--param 0.0 1.0 {a1} {a2} --mbdscale 0.0 --silent {coord_path} | "
            f"grep 'Dispersion energy:' | awk '{{print $3}}'"
        )
        command_s9 = (
            f"{self.dftd4_path} --charge {molecule_charge} --input coord "
            f"--param 0.0 0.0 {a1} {a2} --mbdscale 1.0 --silent {coord_path} | "
            f"grep 'Dispersion energy:' | awk '{{print $3}}'"
        )

        result_s6 = subprocess.run(command_s6, shell=True, text=True,
                                   capture_output=True)
        result_s8 = subprocess.run(command_s8, shell=True, text=True,
                                   capture_output=True)
        result_s9 = subprocess.run(command_s9, shell=True, text=True,
                                   capture_output=True)

        if (result_s6.returncode == 0 and result_s8.returncode == 0 and
            result_s9.returncode == 0):
            return {
                's6': float(result_s6.stdout.strip()),
                's8': float(result_s8.stdout.strip()),
                's9': float(result_s9.stdout.strip())
            }
        else:
            print("Error running command:", result_s6.stderr)
            return None

    def calculate_dispersion_energies(self, testset_name: str,
                                      a1: float, a2: float) -> None:
        """
        Calculates dispersion energies for each molecule in the test set.
        The results are stored in the attribute 'dispersion_energy_results'.

        Parameters:
            testset_name (str): Name of the test set.
            a1 (float): Parameter a1 for dispersion energy calculation.
            a2 (float): Parameter a2 for dispersion energy calculation.
        """
        self.dispersion_energy_results = {}
        for molecule, charge in self.charges.items():
            # Use instance attribute 'base_path' instead of hardcoded path
            coord_path = f"{self.base_path}/{testset_name}/{molecule}/coord"
            energy = self._run_dftd4(a1, a2, coord_path, charge)
            if energy is not None:
                self.dispersion_energy_results[molecule] = energy
            else:
                print(f"Error calculating energy for {molecule}.")

