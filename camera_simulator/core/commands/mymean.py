import numpy as np

from camera_simulator.core.sensor import Sensor


def execute():
    size = (1080, 1920)
    image = (np.random.random(size=size) * 255).astype('uint8')
    sensor = Sensor(gain=2, enable=True)
    gain_image = sensor.process(image)
    output = np.mean(gain_image)
    return output


if __name__ == '__main__':
    mean = execute()
    print(f'mean: {mean}')


