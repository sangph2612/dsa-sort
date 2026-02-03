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

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

for fname, is_float in files:
    data = load_data(fname, is_float)

    start = time.perf_counter()
    if data:
        mergeSort(data, 0, len(data) - 1)
    end = time.perf_counter()

    print(f"{fname}: {end - start:.4f} seconds")
