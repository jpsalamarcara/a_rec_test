import concurrent.futures

from camera_simulator.core.commands import mymean


def test_concurrent_mymean():
    output = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for i in range(0, 100):
            futures.append(executor.submit(mymean.execute))
        for future in concurrent.futures.as_completed(futures):
            output.append(future.result())
    assert len(output) == 100
