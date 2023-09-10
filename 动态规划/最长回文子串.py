"""
题目：https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=295&tqId=25269&ru=%2Fpractice%2F5164f38b67f846fb8699e9352695cd2f&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=

对于长度为n的一个字符串A（仅包含数字，大小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。

"""

class Solution:
    def getLongestPalindrome_my(self , A: str) -> int:
        # 我的暴力解法

        if not A:
            return 0
        n = len(A)
        if n == 1:
            return 1

        def judge(s:str):
            # 判断是否为回文串
            n = len(s)
            middle = int(n / 2)
            if n % 2 == 0:
                if s[:middle] == s[middle:][::-1]:
                    return True
                else:
                    return False
            else:
                if s[:middle] == s[middle + 1:][::-1]:
                    return True
                else:
                    return False

        max_len = 0
        res = ''
        for i in range(n - 1):
            for j in range(i + 1, n +1):
                if judge(A[i:j]):
                    res = A[i:j] if len(A[i:j]) > max_len else res
                    max_len = len(res)
            
        return max_len
    
    def getLongestPalindrome(self , A: str) -> int:
        # 中心扩展法
        n = len(A)
        if n == 1:
            return 1
        
        def expand_around_center(A, left, right):
            while left >= 0 and right < len(A) and A[left] == A[right]:
                left -= 1  # 向左右两边扩展
                right += 1
            return A[left + 1 : right] # 注意返回结果要加回去
        
        longest_palindrome = ''
        for i in range(n):
            # 考虑回文串长度为奇数的情况
            odd = expand_around_center(A, i, i)
            if len(odd) > len(longest_palindrome):
                longest_palindrome = odd

            # 考虑回文串长度为偶数的情况
            even = expand_around_center(A, i, i + 1)
            if len(even) > len(longest_palindrome):
                longest_palindrome = even

        return len(longest_palindrome)