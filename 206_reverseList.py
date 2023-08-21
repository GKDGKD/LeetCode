from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []

        prev    = None
        current = head
        while current:
            next_node    = current.next
            current.next = prev
            prev         = current
            current      = next_node

        return prev
    
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    nodes = [ListNode(i) for i in range(1, 6)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    head = nodes[0]
    print('反转前链表：')
    print_list(head)

    new_head = Solution().reverseList(head)
    print('反转后链表: ')
    print_list(new_head)
