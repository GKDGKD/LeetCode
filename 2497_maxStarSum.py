import heapq
from typing import List
from heapq import nlargest

# 枚举+排序
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = [[] for _ in vals]
        for x, y in edges:
            if vals[y] > 0: g[x].append(vals[y])
            if vals[x] > 0: g[y].append(vals[x])
        return max(v + sum(nlargest(k, a)) for v, a in zip(vals, g))

# class Solution:
#     def maxStarSum(self, vals, edges, k: int) -> int:
#         if len(vals) == 1:
#             return vals[0]

#         def points(edges, vals):
#             star = {i: {'val':vals[i],'degree': 0, 'neighbor': []}
#                         for i in range(len(vals))}
#             for i in edges:
#                 for index, j in enumerate(i):
#                     star[j]['degree'] += 1
#                     if index == 0:
#                         star[j]['neighbor'].append(i[1])
#                     else:
#                         star[j]['neighbor'].append(i[0])

#             return star

#         star = points(edges, vals)
#         s = sorted(filter(lambda x: x[1]['degree'] <= k, star.items()))
#         # (1, {'val': 2, 'degree': 3, 'neighbor': [0, 2, 3]})
#         res = []
#         for i in s:
#             tmp = [i[0]] + i[1]['neighbor']
#             tmp_val = [vals[j] for j in tmp]
#             res.append(heapq.nlargest(k + 1, tmp_val)) # 2条边对应3个节点

#         return max([sum(i) for i in res]), star
            

if __name__ == "__main__":
    edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
    vals = [1,2,3,4,10,-10,-20]
    k = 2

    # vals = [1,-8,0]
    # edges = [[1,0],[2,1]]
    # k = 2

    sol = Solution()
    res = sol.maxStarSum(vals, edges, k)

    # res, star = sol.maxStarSum(vals, edges, k)
    print(res)
    # print(star)
    