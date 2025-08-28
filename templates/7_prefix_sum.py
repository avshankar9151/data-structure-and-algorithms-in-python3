'''
Prefix Sum
------------------------------------------
Use when:

- Range sum queries (fast calculation of sum in subarray).

- 2D prefix sum for matrix queries.

- Problems like “maximum average subarray”, “subarray divisible by K”.
------------------------------------------
'''

def prefix_sum(arr):
    n = len(arr)
    ps = [0] * (n+1)
    for i in range(n):
        ps[i+1] = ps[i] + arr[i]
    return ps

# Range sum query [l, r]
# ps[r+1] - ps[l]
