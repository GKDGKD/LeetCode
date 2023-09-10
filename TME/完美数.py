
"""
完美数：当且仅当该数仅有一个非零数字。如5000， 4， 1， 10，200.

小红拿到了一个大小为n的数组她希望选择两个元素，满足它们的乘积为完美数。问有多少不同的种取法？

"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param arr int整型一维数组 
# @return int整型
#
from typing import  List
from collections import Counter

class Solution:
    def perfectPair(self , arr: List[int]) -> int:
        # write code here
        if len(arr) < 2:
            return 0
        arr = list(set(arr))  # 有重复值
        n = len(arr)

        def judge(num):
            # 判断是否为完美数
            s = str(num)
            if len(s) == 1 and s != '0':
                return True

            s2 = set(s)
            if min(s2) == '0' and len(s2) == 2:
                return True
                
            return False
                
        res = []
        for i in range(n - 1):
            a = arr[i]
            print(f'res: {res}')
            for j in range(i + 1, n):
                b = arr[j]
                num = a * b
                print(f'i: {i}, j: {j}, a: {a}, b: {b}, num: {num}')
                if judge(num):
                    res.append([a, b])
                
        return len(res)
    
sol = Solution()  # 通过5%
print(sol.perfectPair([25,2,1,16]))  

def judge(num):
    # 判断是否为完美数
    s = str(num)
    if len(s) == 1 and s != '0':
        return True
    
    s2 = set(s)
    if len(s2) == 2 and min(s2) == '0':
        return True
    
    return False


## GPT的答案
def countPerfectPairs(arr):
    n = len(arr)
    count = Counter(arr)
    result = 0

    for i in range(1, n + 1):
        if isPerfect(i):
            j = 1 if i == 1 else i // 2  # 找到与 i 相乘得到完美数的 j
            if i == j:
                result += count[i] * (count[i] - 1) // 2  # 组合数 C(count[i], 2)
            else:
                result += count[i] * count[j]

    return result

def isPerfect(num):
    # 判断一个数字是否是完美数
    while num > 0:
        digit = num % 10
        if digit != 0 and num % digit != 0:
            return False
        num //= 10
    return True

# 示例用法
arr = [5000, 4, 1, 10, 200]
result = countPerfectPairs(arr)
print(result)  # 输出结果