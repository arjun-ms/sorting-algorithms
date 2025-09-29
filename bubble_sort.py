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


"""
Bubble Sort: Imagine kids standing in a line, and they keep comparing themselves with the one next to them. 
If someone is taller than the one beside them, they swap places. 
After a lot of swapping rounds, the tallest kid “bubbles up” to the end, then the second tallest, and so on.

👉 It repeatedly swaps neighbors until the list is sorted.
"""
