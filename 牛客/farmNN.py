class Solution:
    def FarmerNN(self , n , m ):
        # write code here

        rounds = m // n  # 奇数正向，偶数反向
        a = [rounds] * n
        left = m % n
        print(f'rounds: {rounds}, a: {a}, left: {left}')
        if rounds % 2 == 1: # 正向
            for i in range(left):
                a[i+1] += 1
            # a[1:left+1] = [i+1 for i in a[1:left+1]]
        else:
            for i in range(-2, -left, -1):
                a[i] += 1
            # a[-(left+1):-1] = [i+1 for i in a[-(left+1):-1]]

        return a
    
sol = Solution()
print(sol.FarmerNN(4, 6)) # [1,2,2,1]
print(sol.FarmerNN(2, 5)) # [3,2]
# print(sol.FarmerNN(197, 738))