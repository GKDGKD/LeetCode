"""
题目来源：https://leetcode.cn/problems/minimum-size-subarray-sum/
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 

思路：
滑动窗口法。本质是用左右指针来减少循环的次数，适合用于求解 最短/最长子数组长度 的题目。

算法步骤：
1. 初始化：固定左右指针为0，得到窗口 [left, right] = [0, 0]；
2. 寻找可行解：固定左指针left不变，右指针right逐渐增大，求解满足条件的窗口[left, right]。
3. 优化已有解：找到解后固定右指针不变，逐步增加左指针，并更新最小长度的结果，直到不满足条件为止。
重复步骤2,3，直到右指针到达数组尽头。

"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)

        left    = 0
        n       = len(nums)
        min_len = n + 1
        sum_    = 0

        for right in range(n):
            sum_ += nums[right]  # 不要直接算sum(nums[left:right])，这样计算开销大
            while sum_ >= target:
                min_len  = min(min_len, right - left + 1)
                sum_    -= nums[left]
                left    += 1
        
        return 0 if min_len > n else min_len
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))  # 2
    print(sol.minSubArrayLen(4, [1,4,4]))  # 1
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # 0
    