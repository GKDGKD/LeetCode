#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def kawaiiStrings(self , n: int) -> int:
        # write code here
        if n < 4:
            return 0
        
        # 1,2,3 = 0; 4:3, 5:18

        a, b = 0, 3
        for i in range(3, n):
            a, b = b, 6*b
        
        return a % (10**9 + 7)