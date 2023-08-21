## 我得解法
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        num = 0
        length = len(s)
        i = 0
        while i < length:
            # print(f'i = {i}, length = {length}')
            if i < length - 1 and table[s[i]] < table[s[i+1]]:
                num += (table[s[i+1]] - table[s[i]])
                i += 2
            else:
                num += table[s[i]]
                i += 1

        # num += table[s[length-1]]
        return num

        