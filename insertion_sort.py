def insertion_sort(arr):
    n = len(arr)
  
    # Start from second element
    for i in range(1, n):
        key = arr[i]         # element to be placed
        j = i - 1
        # shift larger elements to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] 
            j -= 1
        # place the key in its correct position
        arr[j + 1] = key
    return arr


