"""
题目：https://leetcode.cn/problems/minimum-window-substring/

解决这个问题的一种常见方法是使用滑动窗口（Sliding Window）技巧。具体步骤如下：

1. 创建两个指针，left 和 right，分别表示滑动窗口的左边界和右边界，初始都指向字符串 s 的第一个字符。

2. 创建一个字典 need_dict，用于记录字符串 t 中每个字符的出现次数。

3. 创建一个字典 window_dict，用于记录滑动窗口中每个字符的出现次数。

4. 初始化变量 left 和 right，分别表示滑动窗口的左边界和右边界，初始值为 0。

5. 初始化变量 valid，表示滑动窗口中已经满足条件的字符个数，初始值为 0。

6. 初始化变量 start，表示最小覆盖子串的起始位置，初始值为 0。

7. 初始化变量 min_len，表示最小覆盖子串的长度，初始值为正无穷大。

8. 开始移动右边界 right，扩大窗口，直到满足包含字符串 t 中所有字符的条件。

9. 当满足条件时，开始移动左边界 left，缩小窗口，尽量减小子串长度，同时更新最小覆盖子串的起始位置和长度。

10. 重复步骤 8 和 9，直到 right 达到字符串 s 的末尾。

11. 返回最小覆盖子串，即 s[start:start+min_len]。

"""

class Solution:
    def minWindow_gpt(self, s: str, t: str) -> str:
 
        need_dict = {}
        window_dict = {}
        
        # 初始化 need_dict
        for char in t:
            need_dict[char] = need_dict.get(char, 0) + 1
        
        left, right = 0, 0
        valid = 0
        start = 0
        min_len = float('inf')
        
        while right < len(s):
            # 移动右边界
            char = s[right]
            right += 1
            
            if char in need_dict:
                window_dict[char] = window_dict.get(char, 0) + 1
                if window_dict[char] == need_dict[char]:
                    valid += 1
            
            # 判断是否满足条件
            while valid == len(need_dict):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left
                
                # 移动左边界
                char = s[left]
                left += 1
                
                if char in need_dict:
                    if window_dict[char] == need_dict[char]:
                        valid -= 1
                    window_dict[char] -= 1
        
        return "" if min_len == float('inf') else s[start:start+min_len]
    

    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""

        # 滑动窗口法
        # need_dict = {i: 1 for i in t}  # 不能这么写，有些重复的char会也需要算入内
        # window_dict = {i: 0 for i in s}
        need_dict = {}
        window_dict = {}
        left, right = 0, 0
        valid = 0
        start = 0
        min_len = float('inf')

        for char in t:
            need_dict[char] = need_dict.get(char, 0) + 1
        
        while right < m:
            # 移动右边界
            char = s[right]
            right += 1

            if char in need_dict:
                # window_dict[char] += 1
                window_dict[char] = window_dict.get(char, 0) + 1
                if window_dict[char] == need_dict[char]:
                    valid += 1
            
            # 判断是否满足条件
            while valid == len(need_dict):
                # 更新最小子串
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # 移动左边界
                char = s[left]
                left += 1

                if char in need_dict:
                    # 减少重复，获得最短子串
                    if window_dict[char] == need_dict[char]:
                        valid -= 1
                    window_dict[char] -= 1
            
        return "" if min_len == float('inf') else s[start:start+min_len]
        

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow('ADOBECODEBANC', 'ABC'))  # "BANC"
    print(sol.minWindow('aa', 'aa'))  # "aa"