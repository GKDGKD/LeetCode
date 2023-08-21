"""
给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。 
你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。并输出这条最长路径的长度。
这个路径必须满足以下条件：

1. 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
2. 你不能走重复的单元格。即每个格子最多只能走一次。

解法：
这是一个典型的深度优先搜索（DFS）问题，可以通过递归的方式来解决。
我们可以从矩阵的每个单元格出发，尝试在满足条件的情况下进行深度搜索，找到一条递增路径。
在这个示例中，find_increasing_path函数遍历矩阵的每个单元格，并以每个单元格为起点进行深度搜索。
函数dfs用于实现递归的深度搜索，寻找递增路径。当找到一条合适的路径时，它会返回路径上的单元格坐标。

"""

from typing import List

class Solution:
    def solve(self , matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右、左、下、上

        # 用dp存储最长路径长度
        dp = [[0]*cols for _ in range(rows)]

        def dfs(matrix, dp, i, j):
            # 深度优先，单点遍历4个方向，寻找可行解
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] += 1
            
            for dx, dy in directions:
                x_new, y_new = i + dx, j + dy
                print(f'dfs: i:{i}, j:{j}, x_new:{x_new}, y_new:{y_new}, dp[i][j] = {dp[j][j]}')
                # 可能是python版本原因，牛客需要0 <= x_new < rows and 0 <= y_new < cols才能通过测试
                if 0 <= x_new < rows and 0 <= y_new < cols and matrix[x_new][y_new] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(matrix, dp, x_new, y_new) + 1)

            return dp[i][j]
        
        # 遍历矩阵的每个点
        res = 0
        for i  in range(rows):
            for j in range(cols):
                res = max(res, dfs(matrix, dp, i, j))
        
        return res      

if __name__ == "__main__":
    
    # 示例矩阵
    matrix = [
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]

    sol = Solution()
    result = sol.solve(matrix)
    print(result)
