import numpy as np
from scipy.optimize import minimize
from optimization_utils import loss_wrapper, gradient_wrapper, make_callback
from typing import Any, Dict, List, Tuple
from loss_and_gradient_cache import LossAndGradientCache


def _generate_start_point(bounds: List[Tuple[float, float]]) -> np.ndarray:
    """
    Generates a random starting point within the given bounds.

    Parameters:
        bounds: List of tuples representing parameter bounds.

    Returns:
        np.ndarray: Random starting point.
    """
    return np.array([np.random.uniform(low, high) for (low, high) in bounds])


def _is_far_enough(point: np.ndarray, other_points: List[np.ndarray],
                   min_dist: float) -> bool:
    """
    Checks if a point is far enough from all other points.

    Parameters:
        point: The point to check.
        other_points: List of other points.
        min_dist: Minimum distance threshold.

    Returns:
        bool: True if the point is far enough, False otherwise.
    """
    return all(np.linalg.norm(point - other) >= min_dist for other in other_points)


def _optimize_from_point(cache: LossAndGradientCache, point: np.ndarray,
                         index: int):
    """
    Optimizes starting from a specific point.

    Parameters:
        cache: An instance of LossAndGradientCache.
        point: Starting point for optimization.
        index: Index of the optimization run.

    Returns:
        Optimization result.
    """
    result = minimize(
        lambda params: loss_wrapper(cache, params),
        point,
        method='BFGS',
        jac=lambda params: gradient_wrapper(cache, params),
        callback=make_callback(index, cache)
    )
    filename = f'out_{index}.txt'
    with open(filename, 'a') as file:
        file.write("\nFinal parameters:" + str(result.x))
        file.write("\nLoss function:" + str(result.fun))
    return result


def multistart_optimization_parallel(
    data_all: Dict[str, Any],
    initial_params: Any,
    optimize_indices: List[int],
    bounds: List[Tuple[float, float]],
    N: int = 10,
    min_dist: float = 0.1,
    max_attempts: int = 50
):
    """
    Performs multistart optimization with parallel attempts.

    This function instantiates a LossAndGradientCache and performs
    optimization starting from multiple initial points generated within
    the given bounds.

    Parameters:
        data_all (Dict[str, Any]): Data required for loss computation.
        initial_params (Any): Fixed parameters not subject to optimization.
        optimize_indices (List[int]): Indices of parameters to optimize.
        bounds (List[Tuple[float, float]]): List of tuples representing
            parameter bounds.
        N (int): Number of starting points.
        min_dist (float): Minimum distance between starting points.
        max_attempts (int): Maximum attempts to generate a starting point.

    Returns:
        The best optimization result.
    """
    # Instantiate the cache inside the function.
    cache = LossAndGradientCache(
        num_params=len(optimize_indices),
        data_all=data_all,
        fixed_params=initial_params,
        optimize_indices=optimize_indices
    )

    start_points = []
    for _ in range(N):
        attempts = 0
        while attempts < max_attempts:
            new_point = _generate_start_point(bounds)
            if _is_far_enough(new_point, start_points, min_dist):
                start_points.append(new_point)
                break
            attempts += 1

    results = [_optimize_from_point(cache, sp, i)
               for i, sp in enumerate(start_points)]
    best_result = min(results, key=lambda x: x.fun)
    return best_result

