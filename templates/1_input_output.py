'''
Input/Output Template (Fast I/O)
------------------------------------------
Use when:

- Competitive programming (large input size, e.g. Codeforces, AtCoder, etc.)

- Problems with up to 10^6 or more inputs
❌ Not needed in interviews (normal input() is fine).
------------------------------------------
'''

import sys
input = sys.stdin.readline

# Example usage
n, m = map(int, input().split())
arr = list(map(int, input().split()))
