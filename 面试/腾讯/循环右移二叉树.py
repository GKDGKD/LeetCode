"""
现有一棵
�
n个节点构成的二叉树，请你将每一层的节点向右循环位移
�
k位。某层向右位移一位(即
�
=
1
k=1)的含义为：
1.若当前节点为左孩子节点，会变成当前节点的双亲节点的右孩子节点。
2.若当前节点为右儿子，会变成当前节点的双亲节点的右边相邻兄弟节点的左孩子节点。(如果当前节点的双亲节点已经是最右边的节点了，则会变成双亲节点同级的最左边的节点的左孩子节点)
3.该层的每一个节点同时进行一次位移。
4.是从最下面的层开始位移，位移完每一层之后，再向上，直到根节点，位移完毕。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def cyclicShiftTree(self , root: TreeNode, k: int) -> TreeNode:
        # write code here
        if k < 1:
            return root

        # 层序遍历
        def level_order_traverse(root):
            if not root:
                return []
            
            deque = [root]
            res = []

            while deque:
                # 逐层遍历
                level_size = len(deque)
                level_nodes = []
                
                for _ in range(level_size):
                    node = deque.pop(0)
                    level_nodes.append(node.val)
                    
                    if node.left:
                        deque.append(node.left)  # 将左子树入队
                    if node.right:
                        deque.append(node.right) # 将右子树入队
                    
                res.append(level_nodes)

            return res
        
        # 先进行层序遍历，得到每一层的节点列表
        levels = level_order_traverse(root)

        for level in levels:
            level_size = len(level)
            # 计算位移后的索引位置
            rotated_level = [level[(i - k) % level_size] for i in range(level_size)]

            # 更新该层的左右子节点
            for i in range(level_size):
                node = level[i]
                if i > 0:
                    node.left = rotated_level[i - 1]
                if i < level_size - 1:
                    node.right = rotated_level[i + 1]
                else:
                    node.right = None

        return levels[0][0]  # 返回根节点 failed
    

        