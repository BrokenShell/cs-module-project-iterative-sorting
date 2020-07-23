def linear_search(arr, target):
    """ Linear Search O(N)"""
    for key, val in enumerate(arr):
        if target == val:
            return key
    else:
        return -1


def binary_search(arr, target):
    """ Iterative Binary Search O(log2(N))"""
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = round(start + (end - start) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
