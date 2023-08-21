from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        # 深度优先搜索
        if not node:
            return 0
        
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        self.ans += abs(left_sum - right_sum)
        
        return left_sum + right_sum + node.val