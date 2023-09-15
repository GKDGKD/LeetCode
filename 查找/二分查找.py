"""
https://leetcode.cn/problems/binary-search/

二分查找的基本算法思想为：通过确定目标元素所在的区间范围，反复将查找范围减半，直到找到元素或找不到该元素为止。

"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums or target not in nums:
            return -1
        
        left, right = 0, n - 1
        while left <= right:
            # middle = int((right + left) // 2)
            middle = left + ((right - left) >> 1) # 注意位运算的优先级比加减法低
            print(f'left: {left}, right: {right}, middle: {middle}, nums[middle]: {nums[middle]}')
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1, 3, 5, 6], 5))  # 2
    print(sol.search([-1,0,3,5,9,12], 9))  # 4