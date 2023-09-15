# def lcs(s):
#     if not s:
#         return 0

#     n = len(s)
#     dp = [0] * (n + 1)
#     for i in range(n):
#         for j in range(i):
#             if s[i] == s[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
            
#     return max(dp)

# s = input()
# print(lcs(s))


s = input().strip()
n = len(s)
def getnum(s, n):
    for i in range(n // 2, 0, -1):
        c = 0
        for j in range(0, n - i):
            if s[j] != s[j + i]:
                if n - j <= 2 * i:
                    break
                c = 0
            else:
                c += 1
                if c == i:
                    return c * 2
    return 0
print(getnum(s, n))
