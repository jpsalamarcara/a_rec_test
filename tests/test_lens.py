import numpy as np
import pytest

from camera_simulator.core.lens import Lens


@pytest.fixture(scope='module')
def height() -> int:
    return 1080


@pytest.fixture(scope='module')
def width() -> int:
    return 1920


@pytest.fixture(scope='function')
def instance(height, width) -> Lens:
    return Lens(height=height, width=width, enable=True)


def test_process(instance: Lens, height, width):
    valid_image = (np.random.random(size=(height, width)) * 255).astype('uint8')
    output_image = instance.process(image=valid_image)
    assert np.array_equal(valid_image, output_image), 'images are not equal'


bad_test_cases = [
    (None,),
    ([],),
    (np.array([])),
    ((np.random.random(size=(10, 20)) * 255).astype('uint8'))
]


@pytest.mark.parametrize('case', bad_test_cases)
def test_process_bad_inputs(instance: Lens, case):
    with pytest.raises((AssertionError, ValueError)) as context:
        instance.process(case)


def test_getters_setters(instance: Lens, height, width):
    assert instance.enable
    assert instance.height == height
    assert instance.width == width
    instance.enable = False
    assert not instance.enable
    instance.width = 1
    assert instance.width == 1
    instance.height = 2
    assert instance.height == 2
