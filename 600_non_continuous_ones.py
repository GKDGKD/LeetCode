import time

## https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/
# class Solution:
#     def findIntegers(self, n: int):
#         ## 暴力求解
#         ## 数字可以达到10^9， 数字越大，重复计算越多，会超时
#         cnt = 0
#         for i in range(n + 1):
#             if '11' in bin(i)[2:]:
#                 cnt += 0
#             else:
#                 cnt += 1
        
#         return cnt

class Solution:
    def findIntegers(self, n: int):
        ## 动态规划求解
        self.memo = {}

        def dfs(n:int):
            if n in self.memo:
                return self.memo[n]
            if n == 0:
                return 1
            if n == 1:
                return 2
            
            result = dfs(n - 1) + dfs(n - 2)
            self.memo[n] = result
            return result
        
        return dfs(n)
    

if __name__ == "__main__":
    sol = Solution()
    for n in range(1, 11):
        start_time = time.time()
        res = sol.findIntegers(n)
        print(f'n = {n}, result: {res}, elapsed time: {time.time() - start_time}s')