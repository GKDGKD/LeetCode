"""
桶排序（Bucket Sort）基本思想：

将待排序数组中的元素分散到若干个「桶」中，然后对每个桶中的元素再进行单独排序。

桶排序算法步骤
1. 确定桶的数量：根据待排序数组的值域范围，将数组划分为k个桶，每个桶可以看做是一个范围区间。
2. 分配元素：遍历待排序数组元素，将每个元素根据大小分配到对应的桶中。
3. 对每个桶进行排序：对每个非空桶内的元素单独排序（使用插入排序、归并排序、快排排序等算法）。
4. 合并桶内元素：将排好序的各个桶中的元素按照区间顺序依次合并起来，形成一个完整的有序数组。

"""

# def bucket_sort(nums):
#     if not nums:
#         return []
    
#     n = len(nums)


def bucket_sort(arr):
    if not arr:
        return arr

    # 找到最大值和最小值
    min_val, max_val = min(arr), max(arr)

    # 计算桶的数量，这里选择桶的数量为元素的个数
    bucket_count = max_val - min_val + 1
    buckets = [0] * bucket_count

    # 将元素分配到桶中
    for num in arr:
        buckets[num - min_val] += 1

    # 合并桶中的元素，形成有序序列
    sorted_arr = []
    for i in range(bucket_count):
        sorted_arr.extend([i + min_val] * buckets[i])

    return sorted_arr

# 示例
arr = [3, 6, 1, 9, 4, 2, 7, 5, 8]
arr = [3,4,2,9,1,2,0,2,2,2,5,7,9,10,1,32,55,43,22,2,3,1]
arr = []
sorted_arr = bucket_sort(arr)
print(sorted_arr)
