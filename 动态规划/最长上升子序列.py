"""
题目：https://www.nowcoder.com/practice/5164f38b67f846fb8699e9352695cd2f?tpId=295&tqId=2281434&ru=%2Fpractice%2F6d29638c85bb4ffd80c020fe244baf11&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=

给定一个长度为 n 的数组 arr，求它的最长严格上升子序列的长度。
所谓子序列，指一个数组删掉一些数（也可以不删）之后，形成的新数组。例如 [1,5,3,7,3] 数组，其子序列有：[1,3,3]、[7] 等。但 [1,6]、[1,3,5] 则不是它的子序列。


示例：
in: [3,5,7,1,2,4,6,3,8,9,5,6]
out: 6

"""
from typing import List

class Solution:
    def LIS(self , arr: List[int]) -> int:
        # 动态规划求解
        if not arr:
            return 0

        n = len(arr)

        # dp[i]表示到元素i结尾时，最长子序列的长度，单个数组不需要二维数组
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)