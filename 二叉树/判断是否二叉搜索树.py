"""
题目：
https://www.nowcoder.com/practice/a69242b39baf45dea217815c7dedb52b?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return bool布尔型
#
class Solution:
    def isValidBST(self , root: TreeNode) -> bool:
        # write code here

        # 中序遍历, 左中右
        def inorder_traverse(node):
            if not node:
                return 

            nonlocal prev, isBst
            inorder_traverse(node.left)

            # 替换根节点为：检查当前节点的值是否大于前一个节点的值
            if prev is not None and node.val <= prev.val:
                isBst = False
                return 
            prev = node

            inorder_traverse(node.right)
            
        prev = None  # 用于记录前一个节点的值
        isBst = True # 初始假设是二叉搜索树
        inorder_traverse(root)
        return isBst
            