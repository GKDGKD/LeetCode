"""
【2022】贝壳找房秋招机器学习/数据挖掘工程师笔试卷1
牛妹拿到了一个只由小写字母组成的字符串s，接下来将字符串执行k次操作，每次操作都会把s中ASCII码最小的字母从s中删除，请返回k次操作之后的字符串s。

输入例子：
"caabeefa",2
输出例子：
"ceef"

例子说明：
第1次操作，中ASCII值最小的字母是'a'，删除所有的'a'得  ="cbeef"

第2次操作， 中ASCII值最小的字母是'b'，删除所有的'b'得  ="ceef"

因此最终 ="ceef"

"""

# # 超时了
# class Solution:
#     def NS_String(self , s , k ):
#         # write code here

#         a = [i for i in s]
#         for _ in range(k):
#             min_ = min(a)
#             while min_ in a:
#                 a.remove(min_)

#         return ''.join(a)
    

# class Solution:
#     def NS_String(self , s , k ):
#         temp=sorted(list(set(s)))
#         temp_s=temp[k:]
#         res=""
#         for i in s:
#             if i in temp_s:
#                 res+=i
#         return res

# 作者：FlynnFlag
# 链接：https://www.nowcoder.com/exam/test/72767504/submission?examPageSource=Company&pid=35148677&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany%3FcurrentTab%3Drecommand%26jobId%3D100%26keyword%3D%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%26selectStatus%3D0&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91
# 来源：牛客网

class Solution:
    def NS_String(self , s , k ):
        temp    = sorted(set(s))
        use_s   = temp[k:]
        not_use = temp[:k]
        res     = ''
        for i in s:
            if i not in not_use:
                res += i

        return res

if __name__ == "__main__":
    sol = Solution()
    s = 'caabeefa'
    k = 2
    print(sol.NS_String(s, k))