
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    # 版本一：以第一个元素为左右划分基准，递归排序
    pivot = nums[0]  
    left = [i for i in nums[1:] if i <= pivot]
    right = [i for i in nums[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort2(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    # 版本二：以中间的元素作为左右划分基准，递归排序
    middle = int(n // 2) # 版本
    pivot = nums[middle]
    left = [i for i in nums if i < pivot]
    right = [i for i in nums if i > pivot]
    return quick_sort2(left) + [pivot] + quick_sort2(right)


if __name__ == "__main__":
    nums = [5,2,1,6,2,8,10]
    print(quick_sort(nums))
    print(quick_sort2(nums))