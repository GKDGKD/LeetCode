"""
题目：
https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=295&tqId=991075

动态规划思路：

创建一个二维数组 dp，其中 dp[i][j] 表示字符串 str1 的前 i 个字符和字符串 str2 的前 j 个字符的最长公共子序列的长度。

初始化数组 dp。当两个字符相等时，dp[i][j] 的值等于 dp[i-1][j-1] + 1，表示当前字符在最长公共子序列中，否则取 dp[i-1][j] 和 dp[i][j-1] 中的较大值。

使用动态规划填充整个数组 dp，直到计算出 dp[m][n]，其中 m 和 n 分别是字符串 str1 和 str2 的长度。

通过回溯，从 dp[m][n] 出发，根据 dp 数组的信息构建最长公共子序列。

返回最长公共子序列。

回溯算法：

回溯算法是一种试探性搜索算法，它通过尝试不同的选择，逐步构建问题的解。当遇到一个选择不符合条件的情况时，回溯算法会回退到前一步，尝试其他选择，直到找到问题的解或者确定不存在解为止。回溯算法通常用于解决组合、排列、子集、搜索等问题。

在上面的代码中，回溯算法用于构建最长公共子序列。我们从 dp[m][n] 出发，根据 dp 数组的信息，不断向左上方移动，如果当前字符属于最长公共子序列，则加入到结果中，然后继续向左上方移动，直到回溯到 dp[0][0]，构建出最长公共子序列。

这种动态规划和回溯结合的方法可以高效地找到最长公共子序列，并且可以应用于字符串处理等多种领域。

"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # 最长公共子序列可以不连续

        m, n = len(s1), len(s2)
        if any(len(i) == 0 for i in (s1, s2)):
            return '-1'
            
        # dp[i][j]表示在s1中以i结尾，s2中以j结尾的字符串的最长公共子序列长度。
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:  # 注意下标不能越界
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 状态转移方程，dp[i][j]等于上一个dp + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        # 回溯寻找最长公共子序列
        i, j = m, n
        lcs = []
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                lcs.append(s1[i - 1])  # 注意这是从后往前入栈的
                i -= 1  # 向表格的左上角搜索
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
            
        lcs = lcs[::-1]  # 最长公共子序列是逆序的，需要反转
        if len(lcs) == 0:
            return '-1'
        else:
            return ''.join(lcs)
                    