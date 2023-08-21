"""
题目链接：https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46

输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

输入描述：
输入分为是3段，第一段是第一个链表的非公共部分，第二段是第二个链表的非公共部分，第三段是第一个链表和第二个链表的公共部分。 后台会将这3个参数组装为两个链表，并将这两个链表对应的头节点传入到函数FindFirstCommonNode里面，用户得到的输入只有pHead1和pHead2。
返回值描述：
返回传入的pHead1和pHead2的第一个公共结点，后台会打印以该节点为头节点的链表。

示例1
输入：
{1,2,3},{4,5},{6,7}

返回值：
{6,7}

说明：
第一个参数{1,2,3}代表是第一个链表非公共部分，第二个参数{4,5}代表是第二个链表非公共部分，最后的{6,7}表示的是2个链表的公共部分
这3个参数最后在后台会组装成为2个两个无环的单链表，且是有公共节点的   

示例2
输入：
{1},{2,3},{}

返回值：
{}

说明：
2个链表没有公共节点 ,返回null，后台打印{}  

Solution:
要找出两个链表的第一个公共节点，可以使用双指针的方法。
假设两个链表分别为链表A和链表B，我们可以分别用指针pA和pB来遍历两个链表。
由于链表A和链表B可能长度不同，但它们的公共部分一定是在尾部，所以在遍历过程中，
如果pA到达链表末尾，则将pA重定向到链表B的头部，同样，如果pB到达链表末尾，则将pB重定向到链表A的头部。
这样，pA和pB都会在公共部分相遇。

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
        
    return pA

# 示例
# 构造链表A: 1 -> 2 -> 3
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)

# 构造链表B: 6 -> 5 -> 2 -> 3
headB = ListNode(6)
headB.next = ListNode(5)
headB.next.next = headA.next  # 公共部分

result = getIntersectionNode(headA, headB)
if result:
    print("第一个公共结点的值为:", result.val)
else:
    print("链表A和链表B没有公共结点")
