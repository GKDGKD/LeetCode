"""
有一个NxM的整数矩阵，矩阵的行和列都是从小到大有序的。请设计一个高效的查找算法，查找矩阵中元素x的位置。
给定一个int有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，请返回一个二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。
测试样例：
[[1,2,3],[4,5,6]],2,3,6返回：[1,2]
示例1
输入
[[1,2,3],[4,5,6]],2,3,6
输出
[1,2]
"""

def searchMatrix(mat, n, m, x):
    row, col = 0, m - 1  # 从右上角开始
    while row < n and col >= 0:
        if mat[row][col] == x:
            return [row, col]
        elif mat[row][col] < x:
            row += 1  # 往下一行查找
        else:
            col -= 1  # 往左一列查找
    return None  # 没有找到

# 测试
matrix = [[1, 2, 3], [4, 5, 6]]
n = 2
m = 3
x = 6
print(searchMatrix(matrix, n, m, x))  # 输出 [1, 2]
