# Camera Simulator by Juan

## For packaging
```shell
sh package.sh
```

## For running test in local environment
```shell
python3 -m pip install -r dev_requirements.txt
python3 -m pip install -r requirements.txt
pytest tests/ .
```

## For running test in docker environment
```shell
sh run_tests_docker.sh
```