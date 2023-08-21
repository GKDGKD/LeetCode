## 我的初步方法，failed，输入数据类型为ListNode，不是list
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __len__(self):
#         return len(self.val)

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l1_num = sum([l1[i]*10**i for i in range(len(l1))])
#         l2_num = sum([l2[i]*10**i for i in range(len(l2))])
#         two_sum = l1_num + l2_num
#         out = [int(i) for i in str(two_sum)][::-1]

#         return out


# chatgpt给出的答案，可以通过
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # 创建一个虚拟头节点
    current = dummy  # 当前节点指针
    carry = 0  # 进位值
    
    while l1 or l2:
        # 获取当前节点的值，如果链表已经遍历完了，则默认为0
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        # 计算当前节点的和，并加上进位值
        sum = x + y + carry
        
        # 更新进位值和当前节点的值
        carry = sum // 10
        current.next = ListNode(sum % 10)
        
        # 移动指针到下一个节点
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # 处理最后的进位
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy.next  # 返回结果链表的头节点

# 示例测试
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

# 输出结果链表的值
while result:
    print(result.val)
    result = result.next


# ## 官方答案
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         head = point = ListNode(0)  # 将当前节点初始化为返回列表的哑结点
#         carry = 0  # 进位

#         while l1 or l2:  # 遍历l1和l2
#             new_point = ListNode(0)

#             if not l1: # 若达到l1末尾，则只计算l2
#                 sum_ = l2.val + carry
#                 new_point.val = sum_ % 10
#                 carry = sum_ // 10
#                 l2 = l2.next

#             elif not l2:  # 若达到l1末尾，则只计算l2
#                 sum_ = l1.val + carry
#                 new_point.val = sum_ % 10
#                 carry = sum_ // 10
#                 l1 = l1.next

#             else:
#                 sum_ = (l1.val + l2.val + carry)  # sum = x+y+carry

#                 new_point.val = sum_ % 10
#                 carry = sum_ // 10

#                 l1 = l1.next
#                 l2 = l2.next
            
#             point.next = new_point
#             point = point.next

#         if carry: # 检查carry是否为1，是就追加一个含有数字1的新结点
#             new_point = ListNode(1)
#             point.next = new_point

#         return head.next

        

