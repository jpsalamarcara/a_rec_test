import abc

import numpy as np


class BaseProcessor(abc.ABC):
    """
    Abstract class for some good purpose
    """

    def __init__(self, enable: bool):
        self._enable = enable

    @abc.abstractmethod
    def process(self, image: np.ndarray) -> np.ndarray:
        pass  # pragma: no cover

    @property
    def enable(self) -> bool:
        return self._enable

    @enable.setter
    def enable(self, value: bool):
        self._enable = value
