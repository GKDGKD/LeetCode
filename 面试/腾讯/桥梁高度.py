"""

in:
5
2 1 1
3 1 1
5 3 2
5 1 100
4 1 4

out:
1
2
4
-1
4
"""

def out(n, a, b):
    # 桥梁最高处的高度
    # n: 柱子个数，a：第一根柱子高度，b：最后一根逐字高度
    if abs(a - b) >= n:
        print(-1)
        return

    if n == 2:
        print(max(a, b))
        return
    
    if abs(a - b) == n - 1 or abs(a - b) == n - 2:
        print(max(a, b))
        return 
    else:
        print(max(a, b) + 1)
        return 
    
T = int(input())
for _ in range(T):
    n, a, b = map(int, input().split())
    out(n, a, b)
    