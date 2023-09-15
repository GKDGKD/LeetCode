def lcs(s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            
    return max(dp)

s = input()
print(lcs(s))