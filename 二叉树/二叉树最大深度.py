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
# @return int整型
#
class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        if not root:
            return 0

        def getDepth(root):
            if not root:
                return 0
            
            left_height = getDepth(root.left)
            right_height = getDepth(root.right)

            return max(left_height, right_height) + 1
            
        res = getDepth(root)
        return res