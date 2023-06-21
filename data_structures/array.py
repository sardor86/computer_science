import numpy as np


class Array:
    def __init__(self, size: int, dtype) -> None:
        self.size: int = size
        self.dtype = dtype
        self.array: np.ndarray = np.empty(size, dtype=dtype)

    def __str__(self) -> str:
        return str(self.array)

    def __repr__(self) -> str:
        return str(self.array)
