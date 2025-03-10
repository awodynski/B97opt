import numpy as np
from datetime import datetime
from typing import Any, Dict, Tuple

def loss_wrapper(cache: Any, opt_params: np.ndarray) -> float:
    """
    Wrapper function to compute loss using the cache.

    Parameters:
        cache: An instance of LossAndGradientCache.
        opt_params: Parameters for which the loss is computed.

    Returns:
        float: The computed loss.
    """
    loss, _, _, _, _, _ = cache.loss_and_gradient(opt_params)
    return loss

def _loss_series_wrapper(cache: Any, opt_params: np.ndarray
                         ) -> Tuple[float, float, float, float, 
                                    Dict[str, Any]]:
    """
    Wrapper function to compute loss series using the cache.

    Parameters:
        cache: An instance of LossAndGradientCache.
        opt_params: Parameters for which the loss is computed.

    Returns:
        Tuple: (loss, loss1, loss2, loss3, all_loss)
    """
    loss, _, loss1, loss2, loss3, all_loss = \
        cache.loss_and_gradient(opt_params)
    return loss, loss1, loss2, loss3, all_loss

def gradient_wrapper(cache: Any, opt_params: np.ndarray) -> np.ndarray:
    """
    Wrapper function to compute gradient using the cache.

    Parameters:
        cache: An instance of LossAndGradientCache.
        opt_params: Parameters for which the gradient is computed.

    Returns:
        np.ndarray: The computed gradient.
    """
    _, grad, _, _, _, _ = cache.loss_and_gradient(opt_params)
    return grad

def make_callback(index: int, cache: Any):
    """
    Creates a callback function to log optimization progress.

    Parameters:
        index: Index of the current optimization run.
        cache: An instance of LossAndGradientCache.

    Returns:
        Function: A callback function.
    """
    def _callback(xk: np.ndarray) -> None:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scaled_loss, loss1, loss2, loss3, all_loss = \
            _loss_series_wrapper(cache, xk)
        filename = f'out_{index}.txt'
        with open(filename, 'a') as file:
            file.write(f"\nTime: {current_time}")
            file.write("\n Loss:")
            file.write(str(scaled_loss.numpy()))
            file.write("\n WTMAD-2 (train):")
            file.write(str(loss1.numpy()))
            file.write("\n WTMAD-2 (validate):")
            file.write(str(loss2.numpy()))
            file.write("\n WTMAD-2 (all):")
            file.write(str(loss3.numpy()))
#            file.write("\n all loss:")
#           file.write(str(all_loss))
            file.write("\n Params:")
            file.write(", ".join(map(str, xk)) + "\n")
    return _callback

