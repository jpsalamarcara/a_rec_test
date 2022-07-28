import numpy as np

from camera_simulator.core.common import check_valid_image
from camera_simulator.core.processor import BaseProcessor


class Sensor(BaseProcessor):
    """
    This concrete class can add gain to a given image.
    Fits perfect for simulating different iso levels
    """

    def __init__(self, gain: int, **kwargs):
        super().__init__(**kwargs)
        self._gain = gain

    @property
    def gain(self) -> int:
        return self._gain

    @gain.setter
    def gain(self, value: int):
        self._gain = value

    def process(self, image: np.ndarray) -> np.ndarray:
        """
        This function adds gain to an image.
        :param image: numpy.ndarray
        :return: numpy.ndarray
        """
        check_valid_image(image)
        return self.gain * image
