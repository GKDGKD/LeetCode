"""
题目：请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图
示例：
输入：
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]

输出：
[1, 3, 5]

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def buildTree(preorder, inorder):
    # 前序：根左右； 中序：左根右
    if not preorder:
        return None
    
    root_val   = preorder[0] # 前序遍历的第一个值就是根节点
    root       = TreeNode(root_val)
    root_index = inorder.index(root_val)

    # 递归构建，中序遍历的根节点左边为左子树，右边为右子树
    root.left  = buildTree(preorder[1:root_index+1], inorder[:root_index])
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])

    return root

def right_side_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    print(f'queue: {queue}, len(queue): {len(queue)}')

    while queue:
        size = len(queue)
        # 层序遍历获取右视图
        for i in range(size):
            node = queue.pop(0)  # 逐层弹出，只保存下一层的节点
            print(f'size: {size}, i: {i}, node.val: {node.val}')
            if i == size - 1:  # 只要根节点和最右边的节点
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

if __name__ == "__main__":
    preorder = [1, 2, 4, 5, 3]
    inorder  = [4, 2, 5, 1, 3]
    root     = buildTree(preorder, inorder)
    print(f'root: {root}')

    right_view = right_side_view(root)
    print(f'right view: {right_view}')    
