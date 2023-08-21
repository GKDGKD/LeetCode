from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        # 求中位数
        middle = arr[int((n - 1) / 2)]
        print(f'middle: {middle}')

        val = []  #强度
        for i in range(n):
            val.append(abs(arr[i] - middle))

        dic = dict(zip(arr, val))
        print(f'dic: {dic}')

        res = sorted(arr, key=lambda x: dic[x])
        res = res[::-1]

        # dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # res = [i[0] for i in dic]
        print(f'res: {res}')
        return res[:k]

# 官方题解，双向链表
class Solution_official:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        m = arr[(n-1) // 2]
        res = []
        L, R = 0, n-1
        while k > 0:
            if arr[R] - m >= m - arr[L]:
                res.append(arr[R])
                R -= 1
            else:
                res.append(arr[L])
                L += 1
            k -= 1
        return res


if __name__ == "__main__":
    # arr  = [1,2,3,4,5]
    arr = [6,-3,7,2,11]
    # arr = [-7,22,17,3]
    # arr = [1,1,3,5,5]
    # arr = [6,7,11,7,6,8]
    k = 3
    print(f'arr: {arr}, k: {k}')
    sol = Solution()
    res = sol.getStrongest(arr, k)
    print(res)