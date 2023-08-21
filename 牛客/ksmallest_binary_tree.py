"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。


如何遍历二叉树？前序（根左右），中序（左根右），后序（左右根）
二叉搜索树？（左小右大）
对于某节点，其左子树的所有节点的值都小于该节点的值，右子树的所有节点的值都大于该节点的值。

解法：
1. 中序遍历二叉搜索树，返回有序结果
2. 记录已访问的节点数量，当访问到第k个节点时，就找到了第k小的节点。

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution():
    def kth_smallest(self, root, k):
        # 中序遍历
        def inorder(root):
            if not root:
                return []
            
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        res = inorder(root)
        return res[k-1]
    
if __name__ == "__main__":

    # 构建给定的二叉搜索树
    root             = TreeNode(5)
    root.left        = TreeNode(3)
    root.right       = TreeNode(7)
    root.left.left   = TreeNode(2)
    root.left.right  = TreeNode(4)
    root.right.left  = TreeNode(6)
    root.right.right = TreeNode(8)

    k = 3
    sol = Solution()
    print(sol.kth_smallest(root, k))  # 输出: 4
