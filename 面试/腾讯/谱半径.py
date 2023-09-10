"""

in:
3
1.0 1.0 0.5
1.0 1.0 0.25
0.5 0.25 2.0
1.0 1.0 1.0

out:
2.54

计算矩阵A的谱半径
"""

def caculate(A, v0):
    # 计算矩阵A的谱半径
    # A: 矩阵
    # v0: 初始化向量
    n = len(A)
    m = len(A[0])
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, abs(A[i][j] - v0[i] - v0[j]))
    return res

n = int(input())
A = []
for _ in range(n):
    A.append(list(map(float, input().split())))
    
v0 = list(map(float, input().split()))
print(round(caculate(A, v0), 2))
