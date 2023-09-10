#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor_old(self , number: int) -> int:
        # 递归，会超时
        if number < 1:
            return 0

        dp = {}
        dp[1] = 1
        dp[2] = 2
        if number in dp:
            return dp[number]
        else:
            dp[number] = self.jumpFloor(number - 2) + self.jumpFloor(number - 1)
            return dp[number]
        
    def jumpFloor(self , number: int) -> int:
        # 动态规划，直接迭代
        # 递归
        if number < 1:
            return 0

        dp = {}
        dp[1] = 1
        dp[2] = 2
        if number < 3:
            return dp[number]
        else:
            for i in range(3, number + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
                
        return dp[number]
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.jumpFloor(4))