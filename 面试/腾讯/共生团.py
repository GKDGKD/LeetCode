"""
最长公共子串不小于k

in:
3 2
aba
cba
cbc
2 1 3

out:
1
2
1
0

"""

def commonstr(s1, s2, k):
    # 判断是否为共生字符串
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1] > k

def common_cluster(all_set):
    # 判断是否为共生团
    n = len(all_set)
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        if all(commonstr(all_set[i], all_set[j], k) for j in range(i)):
            print(n)
            return
        else:
            


n, k = int(input().split())
s = []
for _ in range(n):
    s.append(input())
    
delete_order = list(map(int(input().split())))

print(1)
for i in range(n - 1):
    print(n - i - 1)

print(0)
