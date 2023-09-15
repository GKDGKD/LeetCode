from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        if not nums or n < 2:
            return False

        for i in range(n - indexDiff + 1):
            print(f'i: {i}')
            for j in range(i + 1, min(indexDiff + i + 1, n)):
                print(f'i: {i}, j:{j}')
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))  # True
    print(sol.containsNearbyAlmostDuplicate([2, 2], 2, 0))  # True
    print(sol.containsNearbyAlmostDuplicate([1,2,1,1], 1, 0))  # True