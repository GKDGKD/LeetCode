"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

from typing import List
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # 我的解法，failed
#         res = {}
#         res[1] = ['()']
#         res[2] = ['()()', '(())']
        
#         if n < 3:
#             return res[n]
        
#         for i in range(3, n + 1):
#             if i in res:
#                 continue
#             else:
#                 tmp = []
#                 for item in res[i - 1]:
#                     tmp.append('()' + item)
#                     tmp.append(item + '()')
#                     tmp.append('(' + item + ')')
                
#                 res[i] = list(set(tmp))
            
#         return res[n]
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(p, left, right, parens=[]):
            if left:         # 如果还有左括号可以使用，则递归添加左括号
                generate(p + '(', left-1, right)
            if right > left:  # 如果有右括号可以使用（但必须有对应的左括号），则递归添加右括号
                generate(p + ')', left, right-1)
            if not right:    # 如果没有右括号可用，表示一个有效组合，添加到结果列表中
                parens += p,
            return parens

        return generate('', n, n)