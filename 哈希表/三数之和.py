"""
题目：https://www.nowcoder.com/practice/345e2ed5f81d4017bbb8cc6055b0b711?tpId=295&tqId=731&ru=%2Fpractice%2F20ef0972485e41019e39543e8e895b7f&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295

给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。

解法一：双指针解法
如果找到了某个数a，要找到与之对应的另外两个数，三数之和为0，那岂不是只要找到另外两个数之和为−a？这就方便很多了。
"""

from typing import List

class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        # write code here
        if not num or len(num) < 3:
            return []

        n = len(num)
        # 先排序，使返回值满足题目要求
        num.sort()
        if num[0] > 0:
            return []
        
        res = []
        
        # 双指针解法, 固定一个数a，另外两个数相加大于-a则右指针左移，反之左指针右移
        for i in range(n - 2):
            # 去重
            if i > 0 and num[i] == num[i - 1]:
                continue
            a     = num[i]  # 固定值
            left  = i + 1
            right = n - 1
            while left < right:
                sum_ = num[left] + num[right]
                if sum_ == -a:
                    res.append([a, num[left], num[right]])
                    while num[left] == num[left+1] and left + 1 < right:
                        # 去重
                        left += 1
                    while num[right] == num[right - 1] and right - 1 > left:
                        # 去重
                        right -= 1
                    # 更新，双指针向中间收缩
                    left += 1
                    right -= 1
                elif sum_ > -a:
                    right -= 1
                else:
                    left += 1

        return res
            