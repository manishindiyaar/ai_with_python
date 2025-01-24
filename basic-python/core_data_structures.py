# Core Data Structures & Algorithms

# Lists
# Creating a list
# Here we create a simple list of integers.
example_list = [1, 2, 3, 4, 5]
# List comprehensions
# This is a list comprehension that squares each element in example_list.
squared_list = [x**2 for x in example_list]

# Dictionaries
# Creating a dictionary
# Here we create a dictionary with keys as letters and values as numbers.
example_dict = {'a': 1, 'b': 2, 'c': 3}
# Dictionary methods
# This retrieves all the keys from example_dict.
keys = example_dict.keys()

# Sets
# Creating a set
# Here we create a set of unique integers.
example_set = {1, 2, 3, 4, 5}
# Set operations
# This demonstrates a union operation, combining example_set with another set.
union_set = example_set.union({6, 7})

# Tuples
# Creating a tuple
# Here we create a tuple of integers. Tuples are immutable.
example_tuple = (1, 2, 3)

# Basic Algorithms
# Linear search
# Linear search algorithm: Iterates through the array to find the element x.
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary search
# Binary search algorithm: Efficiently finds the position of x using a divide-and-conquer approach.
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Bubble sort
# Bubble sort algorithm: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
