"""
将给定的单链表： 
重新排序为：
要求使用原地算法，不能改变节点内部的值，需要对实际的节点进行交换。
例如：
对于给定的单链表{1,2,3,4}，将其重新排序为{1,4,2,3}.
示例1
输入
{1,2,3,4}
输出
{1,4,2,3}

重新排序单链表需要涉及以下步骤：

1. 找到链表的中间节点，将链表分为两半。
2. 反转后半部分链表。
3. 合并两个链表，交错插入。

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reorderList(self, head):
        if not head or not head.next or not head.next.next: return


        # 用龟兔赛跑法来找到链表的中间节点
        # 龟兔赛跑：两个节点一起走，一个节点每次走两步，一个节点每次走一步
        # 当一个节点走到尽头时，另一个节点就是链表的中间节点
        # 最终slow即为中间节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        prev      = None  # 上一节点
        current   = slow.next  # 保存当前的链表，且为中间节点
        slow.next = None  # 将链表断开，分成两个链表
        while current: 
            # 保存当前节点的下一个节点，因为在反转后会改变 current 的 next 指针
            next_node = current.next
            # 将当前节点的 next 指针指向前一个节点，实现反转
            current.next = prev
            # 移动 prev 指针到当前节点，为下一次迭代做准备
            prev = current
            # 移动 current 指针到下一个节点，进行下一次迭代
            current = next_node
            # 最后 prev 指针会指向反转后的链表的头节点

        # 合并两个链表，交错插入
        p1, p2 = head, prev
        while p2:
            next_p1 = p1.next
            next_p2 = p2.next
            p1.next = p2
            p2.next = next_p1
            p1      = next_p1  # 移动 p1 指针到原链表的下一个节点，为下一次插入做准备
            p2      = next_p2  # 移动 p2 指针到反转链表的下一个节点，为下一次插入做准备
            
# 测试
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # 创建链表
    nodes = [ListNode(val) for val in [1, 2, 3, 4]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        
    head = nodes[0]
    # print((head.val))
    print("Original List:")
    printList(head)

    sol = Solution()
    sol.reorderList(head)

    print("Reordered List:")
    printList(head)
        