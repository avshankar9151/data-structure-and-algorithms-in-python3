'''
Dynamic Programming (Memoization & Tabulation)
------------------------------------------
Use when:

- Problem can be broken into overlapping subproblems.

- Typical examples: Fibonacci, knapsack, coin change, LIS, matrix paths.
⚡ Rule: If recursion is too slow → use Memoization. If constraints are high → use Tabulation.
------------------------------------------
'''

'''Top-Down (Memoization):'''
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

'''Bottom-Up (Tabulation):'''
def fib_tab(n):
    dp = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
