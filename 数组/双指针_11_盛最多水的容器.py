"""
https://leetcode.cn/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        n = len(height)
        if not height or n < 2:
            return 0
        
        left, right = 0, n - 1
        max_v = 0
        while left <= right:
            v = (right - left) * min(height[left], height[right])
            if v > max_v:
                max_v = v
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        ## 超时了 
        # for l in range(n - 1):
        #     for r in range(l + 1, n):
        #         v = (r - l) * min(height[l], height[r])
        #         if v > max_v:
        #             max_v = v
                
        return max_v
