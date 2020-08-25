def quick_sort(array, start=0, end=None) -> list:
    if not array: return -1
    if not end: end = len(array) - 1
    if start >= end: return

    pivot_index = partition(array, start, end)

    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)

    return array

def partition(array, start, end) -> int:
    pivot_index = start
    # Always using the end value as pivot
    pivot_val = array[end]

    for i in range(start, end):
        if array[i] < pivot_val:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1

    array[end], array[pivot_index] = array[pivot_index], array[end]
 
    return pivot_index
