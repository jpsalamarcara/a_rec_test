import numpy as np

from camera_simulator.core.common import check_valid_image
from camera_simulator.core.lens import Lens
from camera_simulator.core.processor import BaseProcessor


class Sensor(BaseProcessor):
    """
    This concrete class can add gain to a given image.
    Fits perfect for simulating different iso levels
    """

    def __init__(self, gain: int, **kwargs):
        super().__init__(**kwargs)
        self._gain = gain
        self._last_image = None

    @property
    def gain(self) -> int:
        return self._gain

    @gain.setter
    def gain(self, value: int):
        self._gain = value

    @Lens(height=1080, width=1920, enable=True)
    def process(self, image: np.ndarray) -> np.ndarray:
        """
        This function adds gain to an image.
        :param image: numpy.ndarray
        :return: numpy.ndarray
        """
        check_valid_image(image)
        self._last_image = image
        return self.gain * image

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration < 10:
            self.iteration += 1
            return self._last_image, self.iteration - 1
        else:
            raise StopIteration
