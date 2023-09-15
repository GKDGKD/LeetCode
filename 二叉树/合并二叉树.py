class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param t1 TreeNode类 
# @param t2 TreeNode类 
# @return TreeNode类
#
class Solution:
    def mergeTrees(self , t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 递归方式合并

        if not t1:
            return t2
        if not t2:
            return t1
        
        head = TreeNode(t1.val + t2.val)
        head.left = self.mergeTrees(t1.left, t2.left)
        head.right = self.mergeTrees(t1.right, t2.right)

        return head
    
    def mergeTrees_deque(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 队列方式合并
        if not t1:
            return t2
        if not t2:
            return t1
        
        queue = []
        queue.append(t1)
        queue.append(t2)
        
        while queue:
            node1, node2 = queue.popleft()
            
            # 合并节点值
            node1.val += node2.val
            
            # 处理左子树
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left
            
            # 处理右子树
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif node2.right:
                node1.right = node2.right
        
        return t1