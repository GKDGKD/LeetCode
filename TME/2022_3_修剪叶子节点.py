"""
题目：https://www.nowcoder.com/exam/test/73153546/submission?examPageSource=Company&pid=33702526&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany%3FcurrentTab%3Drecommand%26jobId%3D100%26keyword%3DTME%26selectStatus%3D0&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91
有一棵有n个节点的二叉树，其根节点为root。修剪规则如下:
1.修剪掉当前二叉树的叶子节点，但是不能直接删除叶子节点
2.只能修剪叶子节点的父节点，修剪了父节点之后，叶子节点也会对应删掉
3.如果想在留下尽可能多的节点前提下，修剪掉所有的叶子节点。请你返回修剪后的二叉树。
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
# @return TreeNode类
#

## 方法一：算层数，小于2层的删除, failed
# class Solution:
#     def getHeight(self, root):
#         if root is None:
#             return 0
#         left_h = self.getHeight(root.left)
#         right_h = self.getHeight(root.right)
#         return max(left_h, right_h) + 1
    
#     def delete_leaves(self, root, depth=0):
#         if not root:
#             return None

#         depth = self.getHeight(root)
#         if depth == 0:
#             # 如果深度为0，表示根节点，不删除
#             return root
#         if depth == 1:
#             # 如果深度为1，表示一级子节点，删除左右子节点
#             root.left = None
#             root.right = None
#             return root
#         else:
#             # 递归处理左右子树
#             root.left = self.delete_leaves(root.left, depth - 1)
#             root.right = self.delete_leaves(root.right, depth - 1)
#             return root

    # def pruneLeaves(self , root: TreeNode) -> TreeNode:
    #     # write code here
    #     max_depth = self.getHeight(root)
    #     if max_depth > 2:
    #         root = self.delete_leaves(root, max_depth - 1)

    #         return root

## 方法二：递归
class Solution:
    def pruneLeaves(self , root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # 左孩子是叶子结点，删除
        if root.left and root.left.left is None and root.left.right is None:
            return None
        if root.right and root.right.left is None and root.right.right is None:
            return None
        
        root.left = self.pruneLeaves(root.left)
        root.right = self.pruneLeaves(root.right)

        return root
        
            
# 打印删除后的二叉树结构
def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

if __name__ == "__main__":
   # 创建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7) 

    printTree(root)
    print('修剪后：\n')
    sol = Solution()
    root = sol.pruneLeaves(root)
    printTree(root)