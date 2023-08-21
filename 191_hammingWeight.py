class Solution:
    def hammingWeight(self, n: int) -> int:
        # 注意输入的数仍然是整数n，而不是二进制数字
        # 暴力解法
        # str_n = bin(n)
        # # nums = [int(i) for i in str_n]  # 有二进制的'b'，没法全部转换为数字
        # # cnt = sum(nums)

        # cnt = 0
        # for i in range(len(str_n)):
        #     if str_n[i] == '1':
        #         cnt += 1
        #     else:
        #         cnt += 0

        # return cnt

        # 简单解法
        return bin(n).count('1')
    

    
if __name__ == "__main__":
    sol = Solution()
    n = 5
    cnt = sol.hammingWeight(n)
    print(cnt)

        