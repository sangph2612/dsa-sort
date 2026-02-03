import time
import random

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

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    swap(arr, pivot_index, high)
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

for fname, is_float in files:
    data = load_data(fname, is_float)

    start = time.perf_counter()
    if data:
        quickSort(data, 0, len(data) - 1)
    end = time.perf_counter()

    print(f"{fname}: {end - start:.4f} seconds")
