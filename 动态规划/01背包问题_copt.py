import time
from coptpy import *

# 创建COPT环境
env = Envr()

def knapsack_01(values, weights, capacity):
    n = len(values)
    
    # 创建模型
    model = env.createModel()
    
    # 创建变量 x[i] 表示第i个物品是否放入背包中
    x = model.addVars(n, vtype=COPT.BINARY, nameprefix="x")
    
    # 设置目标函数：最大化总价值
    model.setObjective(sum(values[i] * x[i] for i in range(n)), sense=COPT.MAXIMIZE)
    
    # 添加容量约束
    model.addConstr(sum(weights[i] * x[i] for i in range(n)) <= capacity, name="Capacity")
    
    # 求解模型
    model.solve()
    
    # 打印最优解
    if model.status == COPT.OPTIMAL:
        selected_items = [i for i in range(n) if x[i].x > 0.5]
        return model.objVal, selected_items
    else:
        return None, None
    
# 示例用法
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
start_time = time.time()
max_value, selected_items = knapsack_01(values, weights, capacity)
print(f'Copt耗时：{time.time() - start_time}s')
print("最大价值:", max_value)
print("选择的物品索引:", selected_items)