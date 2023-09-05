"""
题目：https://www.nowcoder.com/practice/20ef0972485e41019e39543e8e895b7f?tpId=295&tqId=745&ru=%2Fpractice%2F508378c0823c423baa723ce448cbfd0c&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295
"""

class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # 哈希解法
        if not numbers:
            return []

        res = []
        # 创建哈希表，key表示值，value 表示对应的下标
        hashtable = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]  # 查找目标值
            if temp not in hashtable:   # 若不在哈希表中，则将该值存入哈希表中
                hashtable[numbers[i]] = i
            else:
                # 哈希表之前记录的数字比i小，所以不需要再排序
                res.append(hashtable[temp] + 1)
                res.append(i + 1)
                break
        
        return res