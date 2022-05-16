from typing import List
import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        h = nums1 + nums2
        heapq.heapify(h)
        l = len(nums1) + len(nums2)
        if l == 1:
            return heapq.heappop(h)
        if l % 2 == 0:
            for i in range(l // 2 - 1):
                heapq.heappop(h)
            return (heapq.heappop(h) + heapq.heappop(h)) / 2
        else:
            for i in range(l // 2):
                heapq.heappop(h)
            return heapq.heappop(h)