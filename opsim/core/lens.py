import numpy as np

from opsim.core.common import check_valid_image
from opsim.core.processor import BaseProcessor


class Lens(BaseProcessor):
    """
    Lens concrete class, simulates a len of a given size (height, width)
    """

    def __init__(self, height: int, width: int, **kwargs):
        super().__init__(**kwargs)
        self._height = height
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    def process(self, image: np.ndarray) -> np.ndarray:
        """
        This function checks if an image has the same size as the lens.
        If a match happens will return the input image. Else will raise a ValueError exception
        :param image: numpy.ndarray
        :return: numpy.ndarray
        """
        check_valid_image(image)
        h, w = image.shape
        if (h, w) != (self.height, self.width):
            raise ValueError('(height, width) does not match with expected values')
        return image
