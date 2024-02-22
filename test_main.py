import time
from lib.disk import Disk
from lib.data import Data

def test_disk_performance():
    # generate a disk with 1000 data
    test_data = []

    d = Disk(cow=True)
    start_time = time.time()
    for i in range(1000):
        if i % 2 == 0:
            idx = d.write(Data(f"data{i}"))
            test_data.append([idx, f"data{i}"])
        else:
            data_to_update = test_data.pop(0)
            idx = d.update(Data(f"data{i}"), data_to_update[0])
            test_data.append([idx, f"data{i}"])
    end_time = time.time()
    cow_elapsed_time = end_time - start_time
    print(f"Elapsed time with cow=True: {cow_elapsed_time} seconds")
    d.format_disk()
    test_data.clear()
    d.is_cow = False
    start_time = time.time()
    for i in range(1000):
        if i % 2 == 0:
            idx = d.write(Data(f"data{i}"))
            test_data.append([idx, f"data{i}"])
        else:
            data_to_update = test_data.pop(0)
            d.update(Data(f"data{i}"), data_to_update[0])
            test_data.append([idx, f"data{i}"])
    end_time = time.time()
    nocow_elapsed_time = end_time - start_time
    print(f"Elapsed time with cow=False: {nocow_elapsed_time} seconds")
    print(f"Difference(nocow vs cow): {(cow_elapsed_time / nocow_elapsed_time - 1) * 100} %")

test_disk_performance()