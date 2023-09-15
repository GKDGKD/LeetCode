
N, M = map(int, input().split())  # N：攻击阶段，M: 安全策略个数
a = list(map(int, input().split()))  # 阶段扣分
# print(a)
for j in range(M):
    b, k = map(int, input().split())
    v = [b + k*i - a[i] for i in range(N)]
    # print(v)
    print(min(v))


"""
in:
6 4
1 3 5 7 9 11
100 0
100 2
100 3
100 -10

out:
89
99
99
39


"""