from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        max_, min_ = nums[-1], nums[0]
        ans = max_ - min_
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            tmp = max(max_ - k, a + k) - min(min_ + k, b - k)
            ans = min(ans, tmp)

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 6]
    k = 3
    res = sol.smallestRangeII(nums, k)
    print(res)