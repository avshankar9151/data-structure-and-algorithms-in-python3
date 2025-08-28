'''
Binary Search
------------------------------------------
Use when:

- Searching in a sorted array

- Problems like "find first/last occurrence", "search in rotated sorted array", "minimum in sorted rotated array"

- Optimization problems (“minimum x such that condition is true”) → Binary Search on Answer
------------------------------------------
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found
