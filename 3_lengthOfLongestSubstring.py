"""


"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        if n == 1:
            return 1

        max_len = 1

        for i in range(n-1):
            left  = i
            right = i + 1
            res   = s[left]
            print(f'left: {left}, right:{right}, res: {res}, max_len: {max_len}')
            while right < n and s[right] not in res:
                print(f'while: right:{right}, res:{res}')
                res     += s[right]
                right   += 1
                max_len  = max(max_len, len(res))

        print(f'final res: {res}')
        return max_len
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))