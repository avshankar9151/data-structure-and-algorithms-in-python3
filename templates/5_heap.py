'''
Heap (Priority Queue)
------------------------------------------
Use when:

- Always need to fetch the min or max element quickly.

- Dijkstra's algorithm (shortest path).

- “K largest/smallest elements”.

- Merging sorted arrays.
------------------------------------------
'''

import heapq

# Min Heap
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
print(heapq.heappop(min_heap))  # 2

# Max Heap (use negative values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
print(-heapq.heappop(max_heap))  # 8

heapq.nlargest(2, [5, 1, 8, 3])  # [8, 5]
heapq.nsmallest(2, [5, 1, 8, 3])  # [1, 3]
heapq.heappushpop(min_heap, 1)  # Push 1 and pop the smallest element
heapq.heapreplace(min_heap, 4)  # Pop and return the smallest element, then push 4
