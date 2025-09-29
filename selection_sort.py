# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # find the smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the found smallest with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


"""
Selection Sort: Imagine you’re picking teams. 
You look at everyone, find the shortest person, and place them first. 
Then you look at the rest, find the next shortest, and place them second. 
You keep repeating until everyone is lined up by height.

👉 It always looks for the smallest (or largest) in the unsorted group and puts it in the correct spot.
"""
