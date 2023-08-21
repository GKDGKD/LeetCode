import pdb

class Solution:
    def twoSum(self, nums, target: int):
        # 哈希表解法，目标在于快速找到 target - x
        hashtable = dict()
        for i, val in enumerate(nums):
            if target - val  in hashtable:
                return [hashtable[target - val], i]
            hashtable[nums[i]] = i
            print(f'i: {i}, val: {val}, target: {target}, hashtable: {hashtable}')

        # pdb.set_trace()
        return []
    

if __name__ == "__main__":
    s  = Solution()
    out = s.twoSum([2,7,11,5], 9)
    print(f'out: {out}')
