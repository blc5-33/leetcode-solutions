import heapq
from typing import List

# NeetCode Solution
# Heaps are great for keeping some loose sorting upon adding and
# removing some elements.

# NOTE: From pydocs,
# > If I find myself having to use `sorted()` or `min()` or `max()` constantly,
# then consider using a heap, as that will be faster for repeated usage of
# those operations.

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

