from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # z字形打印二叉树
        if not pRoot:
            return []
        
        queue = []
        queue.append(pRoot)
        res  = []
        flag = 0  # 奇偶性判定左右打印顺序，偶数：从左到右；奇数：从右到左

        while queue:
            level_size   = len(queue)
            level_values = []

            for _ in range(level_size):     
                node = queue.pop(0)
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flag % 2 == 0: # 偶数
                res.append(level_values)
            else:
                res.append(level_values[::-1])
            flag += 1

        return res