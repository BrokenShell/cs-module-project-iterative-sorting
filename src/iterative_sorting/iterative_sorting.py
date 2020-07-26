from Fortuna import shuffle
import IteratorAlgorithms as ia


def selection_sort(arr: list, ascending=True) -> list:
    """ Selection Sort
    Inplace, destructive

    DocTests:
    >>> t = list(range(10))
    >>> shuffle(t)
    >>> selection_sort(t)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> shuffle(t)
    >>> selection_sort(t, ascending=False)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    @param ascending: Bool
    @param arr: Input list of numbers
    @return: sorted list
    """
    func = min if ascending else max
    range_to = len(arr) - 1
    for i in range(range_to):
        arr.insert(i, arr.pop(arr.index(func(arr[i:]))))
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(array):
    """ Radix Sort with counting component for extra extra points """

    if not array:
        return []

    if not all(x >= 0 for x in array):
        return "Error, negative numbers not allowed in Count Sort"

    def counting():
        size = len(array)
        output = [0] * size
        count = [0] * 10
        for i in range(size):
            index = array[i] // place
            count[index % 10] += 1
        count = list(ia.partial_sum(count))
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(len(array)):
            array[i] = output[i]

    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting()
        place *= 10

    return array
