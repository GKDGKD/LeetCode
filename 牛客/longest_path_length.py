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

牛客官方题解：
class Solution:
    global dirs
    #记录四个方向
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
    global n, m
    #深度优先搜索，返回最大单元格数
    def dfs(self, matrix:List[List[int]], dp: List[List[int]], i:int, j:int) :
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] += 1
        for k in range(4):
            nexti = i + dirs[k][0]
            nextj = j + dirs[k][1]
            #判断条件
            if  nexti >= 0 and nexti < n and nextj >= 0 and nextj < m and matrix[nexti][nextj] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], self.dfs(matrix, dp, nexti, nextj) + 1)
        return dp[i][j]
    
    def solve(self , matrix: List[List[int]]) -> int:
        global n,m
        #矩阵不为空
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        #i，j处的单元格拥有的最长递增路径
        dp = [[0 for col in range(m)] for row in range(n)]  
        for i in range(n):
            for j in range(m):
                #更新最大值
                res = max(res, self.dfs(matrix, dp, i, j)) 
        return res

# 链接：https://www.nowcoder.com/practice/7a71a88cdf294ce6bdf54c899be967a2
"""

from typing import List

class Solution:
    def is_valid(self, x, y, prev_value, visited, matrix):
        # 判断路径是否有效
        rows, cols = len(matrix), len(matrix[0])
        return 0 < x < rows and 0 < y < cols and not visited[x][y] and matrix[x][y] > prev_value

    def solve(self , matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右、左、下、上

        # def dfs(x, y)

    def find_increasing_path(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右、左、下、上

        def dfs(x, y, prev_value, visited):
            visited[x][y] = True
            max_path_length = 0
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, prev_value, visited, matrix):
                    path_length = dfs(new_x, new_y, matrix[new_x][new_y], visited) + 1
                    max_path_length = max(max_path_length, path_length)
            visited[x][y] = False  # 回溯，重置已访问状态
            return max_path_length

        max_path_length = 0
        for i in range(rows):
            for j in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                path_length = dfs(i, j, matrix[i][j], visited) + 1
                max_path_length = max(max_path_length, path_length)

        return max_path_length

if __name__ == "__main__":
    
    # 示例矩阵
    matrix = [
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]

    sol = Solution()
    result = sol.find_increasing_path(matrix)
    print(result)
