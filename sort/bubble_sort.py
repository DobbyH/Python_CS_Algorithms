def bubble_sort(array):
    """ Bubble sort """
    if not array: return -1

    n = len(array)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                # Swap items
                    array[j], array[j+1] = array[j + 1], array[j]

    return array
