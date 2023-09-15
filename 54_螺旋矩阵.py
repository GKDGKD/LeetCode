"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

https://leetcode.cn/problems/spiral-matrix/description/
"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix

        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1] # 顺时针旋转矩阵
            
        return res