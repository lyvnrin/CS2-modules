# Factorial - iterative 
def factIterative(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

# Factorial - recursive 
def factRecursive(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factRecursive(n - 1)

# Binary Search - iterative
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else: 
            right = mid + 1
    return -1

# Merge Sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge Sort - non-recursive
def mergeSortIterative(arr):
    width = 1
    n = len(arr)
    result = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i:i + width]
            right = result[i + width:i + 2 * width]
            result[i:i + 2 * width] = merge(left, right)
        width *= 2
    return result