docker build -t camera_simulator:testing -f docker/tests_runner.dockerfile .
docker run camera_simulator:testing