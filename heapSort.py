import time

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

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

for fname, is_float in files:
    data = load_data(fname, is_float)

    start = time.perf_counter()
    if data:
        heapSort(data)
    end = time.perf_counter()

    print(f"{fname}: {end - start:.4f} seconds")
