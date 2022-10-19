from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        print(count)
        nums.sort(key = lambda x:(count[x],-x))
        return nums


"""
时间复杂度：0（n1ogn），其中几是数组rums的长度。排序消耗 0（n1ogn）时间。
空间复杂度：0(2），存储数组元素频率的哈希表消耗 O(n）空间，
用数组或者哈希表统计 nums 中每个数字出现的次数m,然后对 nums 按照数字出现次数升序排序，如果出现次数相同，则按照数字降序排序。
"""
if __name__ == '__main__':
    nums = [2, 3, 1, 3, 2]
    print(Solution().frequencySort(nums))