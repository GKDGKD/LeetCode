class Solution:
    def plusOne(self, digits):
        # if len(digits) == 1:
        #     return [digits[0] + 1]
        # else:
        num = 0
        n = len(digits)
        for i in range(n):
            num += digits[i] * 10 ** (n - i - 1)
            
        num += 1
        print(f'num: {num}')
        res = [int(i) for i in str(num)]
        return res

if __name__ == "__main__":
    digits = [9]
    sol = Solution()
    res = sol.plusOne(digits=digits)
    print(f'res: {res}')