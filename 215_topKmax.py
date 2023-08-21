from typing import List
from heapq import heappush, heappop

# 堆排序
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []  #heap构造的是最小堆
#         for i in nums:
#             heappush(heap, i)
#             if len(heap) > k:
#                 heappop(heap)

#         return heap[0]
    
# ## 快排——调用库函数
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums, reverse=True)[k-1]


## 快速排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_sort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]
            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)

        arr = quick_sort(nums)

        return arr[-k]



if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    res = sol.findKthLargest(nums, k)
    print(res)