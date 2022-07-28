import numpy as np


def check_valid_image(image: np.ndarray):
    """
    This function perform several validations over an input image.
    if any validation fail it will raise an AssertionError exception
    :param image: numpy.array
    """
    assert image is not None, 'image must have a value'
    assert type(image) == np.ndarray, 'image must be a numpy.ndarray'
    assert len(image.shape) == 2, 'image must be a 2d numpy.ndarray'
