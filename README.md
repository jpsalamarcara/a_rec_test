# Camera Simulator by Juan

## Comments
* All base work features were implemented
* Did not generate documentation: neither sphinx nor jupyter tutorial (too much time)
* For packaging, testing and docker execution see [technical-details](#technical-details)
* All advanced features were implemented:
  * Decorator: see `camera_simulator.core.sensor.Sensor:27`
  * Iterator: see `tests.test_sensor:41`
  * Entrypoint: see `camera_simulator.core.commands.mymean.execute`
  * Concurrent: see `tests.test_concurrent.test_concurrent_mymean`
* It was fun! 


## Technical Details

### For packaging
```shell
sh package.sh
```

### For running test in local environment
```shell
python3 -m pip install -r dev_requirements.txt
python3 -m pip install -r requirements.txt
pytest tests/ .
```

### For running test in docker environment
```shell
sh run_tests_docker.sh
```