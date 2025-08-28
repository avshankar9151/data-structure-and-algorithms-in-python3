'''
Kadane's Algorithm (Max Subarray Sum)
------------------------------------------
Use when:

- Maximum subarray sum problems.

- Can be extended to circular subarray sum, DP optimization.
------------------------------------------
'''

def max_subarray(arr):
    best = curr = arr[0]
    for num in arr[1:]:
        curr = max(num, curr + num)
        best = max(best, curr)
    return best
