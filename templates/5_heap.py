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
