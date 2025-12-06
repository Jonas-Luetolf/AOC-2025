from typing import Iterable
from functools import reduce

def prod(nums: Iterable[float]) -> float:
    return reduce(lambda x, y: x * y, nums, 1)
