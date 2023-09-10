

class Solution:
    def Fibonacci(self , n: int) -> int:
        # 单纯递归容易超时，用记忆递归
        
        dp = {}
        dp[1] = 1
        dp[2] = 1
        
        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2)
            return dp[n]
        
        return dfs(n)
    
    def Fibonacci2(self , n: int) -> int:
        # 迭代解法
        
        if n < 3:
            return 1

        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b

        return b
        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.Fibonacci(4))