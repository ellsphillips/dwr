import random
from typing import List

import numpy as np


def brownian(
    mu: float = 0.01, sigma: float = 0.1, steps: int = 50, initial_value: float = 5
) -> List[float]:
    np.random.seed(int(100 * random.random()))
    returns = np.random.normal(loc=mu, scale=sigma, size=steps)
    return list(initial_value * (1 + returns).cumprod())  # type: ignore
