rm -dfr dist/
python3 setup.py sdist bdist_wheel
rm -dfr build/ && rm -dfr camera_simulator.egg-info