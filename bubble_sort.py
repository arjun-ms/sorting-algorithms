# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
