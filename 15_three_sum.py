class Solution:
    def threeSum(self, nums):
        # 双指针解法
        result = []
        n = len(nums)
        nums.sort()
        if len(nums) < 3 or nums[0] > 0:
            return []

        for i in range(n - 2):
            # 需要和上一次枚举的数不同
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            # left = i + 1
            right = n - 1
            for left in range(i + 1, n - 1):
                # print(f'len(nums) = {len(nums)}, i: {i}, left: {left}, right: {right}, nums[left] + nums[right] = {nums[left] + nums[right]}')
                # # 需要和上一次枚举的数不同
                if left > i + 1 and nums[left] == nums[left-1]:
                    continue

                # 移动右指针
                while left < right and nums[left] + nums[right] > target:
                    right -= 1

                # 如果左右指针相等，那就是遍历完了，可以跳出当前for循环
                if left == right:
                    break

                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])

        return result
    
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = sol.threeSum(nums)
    print(f'result: {result}')
