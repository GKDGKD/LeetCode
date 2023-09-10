"""



注意这题求的是最长公共子串，不是最长公共子序列，子序列可以是不连续的，但子串一定是连续的。

"""

class Solution:
    def LCS_in(self , str1: str, str2: str) -> str:
        # 枚举做法
        n       = len(str1)
        res     = ''
        left    = 0  #左指针，不同则逐个遍历
        max_len = 0
        for i in range(n + 1):
            if str1[left:i + 1] in str2:
                res = str1[left:i + 1] if len(str1[left:i + 1]) > max_len else res
                max_len = len(res)
            else:
                left += 1

        return res

    def LCS(self , str1: str, str2: str) -> str:
        # 子序列是连续的，动态规划求解，会超时

        m, n = len(str1), len(str2)
        
        # 创建一个二维数组 dp 用于存储最长公共子串的长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化最长公共子串的长度为 0
        max_len = 0
        # 记录最长公共子串的结束位置
        end_index = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i  # 更新最长公共子串的结束位置
                else:
                    dp[i][j] = 0  # 如果不相等，将最长公共子串长度重置为 0
        
        # 根据最长公共子串的结束位置和长度，提取最长公共子串
        longest_common_substring = str1[end_index - max_len:end_index]
        
        return longest_common_substring     