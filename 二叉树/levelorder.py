from typing import List
class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # 用队列实现层序遍历
        if not root:
            return []

        queue = []  # pop弹出栈顶元素，pop(0)弹出栈底元素

        # 将根节点入队
        queue.append(root)
        res = []

        # 逐层遍历
        while queue:
            level_size   = len(queue)  # 该层的元素数量
            level_values = []        # 存储该层的元素

            # 遍历该层的元素
            for _ in range(level_size):
                node = queue.pop(0)             # 出队，注意得是node而不是root，不然一直在root，无法前往下一层
                level_values.append(node.val)   # 存储节点的值

                if node.left:
                    queue.append(node.left)  # 将左子树入队
                if node.right:
                    queue.append(node.right) # 将右子树入队

            res.append(level_values) # 存储该层的结果

        return res

        
        