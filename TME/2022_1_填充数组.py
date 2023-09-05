"""
题目：https://www.nowcoder.com/exam/test/73153546/detail?pid=33702526&examPageSource=Company&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany%3FcurrentTab%3Drecommand%26jobId%3D100%26keyword%3DTME%26selectStatus%3D0&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91

输入例子：
[0,4,5],6
输出例子：
4
例子说明：
所有的合法填充方案是：[1,4,5],[2,4,5],[3,4,5],[4,4,5]，共4种。   

"""

from typing import List

class Solution:
    def FillArray(self , a: List[int], k: int) -> int:
        # write code here
        if not a:
            return 0
        
        
        

    
sol = Solution()
print(sol.FillArray([0,4,5],6)) # 4