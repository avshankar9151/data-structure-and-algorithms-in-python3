'''
Sliding Window
------------------------------------------
Use when:

- Problems on subarrays/substrings of fixed length k (max sum, avg, count distinct).

- Two-pointer problems (variable window size) → longest substring without repeating characters.
------------------------------------------
'''

def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
