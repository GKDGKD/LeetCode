"""
0/1背包问题是背包问题中的一个经典问题，目标是在一定容量的背包容器中，从一组物品中选择放入或不放入，使得放入背包的物品总价值最大化，同时不超过背包的容量限制。

注意每个物品最多只能放入一次。
"""
import time
def knapsack_01(values, weights, capacity):
    # 动态规划求解0/1背包问题

    n = len(values)

    # 创建一个二维数组dp，dp[i][j]表示前i个物品放入容量为j的背包中的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    # 从后往前回溯找出所有选择的物品
    seleced_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            seleced_items.append(values[i - 1])
            j -= weights[i - 1]

    return dp[n][capacity], seleced_items


def sol(values, weights, capacity):
    n = len(values)

    # 背包容量从0到capacity，物品从0到n编号
    # dp[i][j]表示前i个物品放入容量为j的背包中的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1): # 从1开始，0肯定是0
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:  # 物品i无法放入容量为j的背包
                dp[i][j] = dp[i - 1][j]  # 注意i - 1是第i件物品，j表示背包容量，不用j - 1
            else:  # 物品i可以放入容量为j的背包
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    # 回溯找出放入背包的物品清单
    selected = []
    i, j =  n, capacity
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            selected.append(values[i - 1])
            j -= weights[i - 1]

    return dp[n][capacity], selected
    

# 示例用法
values   = [60, 100, 120]
weights  = [10, 20, 30]
capacity = 50
start_time = time.time()
max_value, selected_items = knapsack_01(values, weights, capacity)
# max_value, selected_items = sol(values, weights, capacity)
print(f'动态规划耗时：{time.time() - start_time}s')
print("最大价值:", max_value)
print("选择的物品索引:", selected_items)