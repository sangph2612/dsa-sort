import time
import numpy as np

def load_data(filename, is_float=True):
    with open(filename, "r") as f:
        if is_float:
            return [float(x) for x in f]
        else:
            return [int(x) for x in f]

files = [
    ("datasets/data1.txt", True),
    ("datasets/data2.txt", True),
    ("datasets/data3.txt", True),
    ("datasets/data4.txt", True),
    ("datasets/data5.txt", True),
    ("datasets/data6.txt", False),
    ("datasets/data7.txt", False),
    ("datasets/data8.txt", False),
    ("datasets/data9.txt", False),
    ("datasets/data10.txt", False),
]

def numpySort(arr):
    return np.sort(arr)

for fname, is_float in files:
    data = load_data(fname, is_float)
    arr = np.array(data)
    start = time.perf_counter()
    if data:
        arr = numpySort(arr)
    end = time.perf_counter()

    print(f"{fname}: {end - start:.4f} seconds")
