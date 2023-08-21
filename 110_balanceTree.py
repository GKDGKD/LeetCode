from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # 递归解法
        def getHeight(node: TreeNode):
            if not node:
                return 0
            
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)

            return max(left_height, right_height) +  1

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        
        return abs(left_height - right_height) <= 1

if __name__ == "__main__":
    # root = [3,9,20, None, None, 15,7]
    
    # 创建示例1中的二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # 判断是否是高度平衡的
    sol = Solution()
    result = sol.isBalanced(root)
    print(result)  # 输出：True
