"""
当且仅当该二叉树所有节点的孩子数量为偶数时（0或者2），才能称为好二叉树。
"""

class Solution:
    def cntOfTrees(self , n: int) -> int:
        # write code here
        if n % 2 == 0 or n == 1:
            return 0

        dp = {
            3: 1,
            5: 2,
            7: 5,
            9: 20
        }
        
        if n in dp:
            return dp[n]
        else:
            dp[n] = dp[n - 2] * dp[n - 4]

            return dp[n]