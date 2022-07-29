import numpy as np
import pytest

from camera_simulator.core.sensor import Sensor


@pytest.fixture(scope='module')
def instance() -> Sensor:
    return Sensor(gain=2, enable=True)


def test_process(instance: Sensor):
    size = (1080, 1920)  # This size is defined by default in Lens decorator
    valid_image = (np.random.random(size=size) * 255).astype('uint8')
    output_image = instance.process(image=valid_image)
    assert np.array_equal(2*valid_image, output_image), 'images are equal'


bad_test_cases = [
    (None,),
    ([],),
    (np.array([]))
]


@pytest.mark.parametrize('case', bad_test_cases)
def test_process_bad_inputs(instance: Sensor, case):
    with pytest.raises(AssertionError) as context:
        instance.process(case)


def test_getters_setters(instance: Sensor):
    assert instance.enable
    instance.enable = False
    assert not instance.enable
    assert instance.gain == 2
    instance.gain = 1
    assert instance.gain == 1


def test_iterator(instance: Sensor):
    output = [x for x in instance]
    assert len(output) == 10
    indexes = [x[1] for x in output]
    assert min(indexes) == 0
    assert max(indexes) == 9
