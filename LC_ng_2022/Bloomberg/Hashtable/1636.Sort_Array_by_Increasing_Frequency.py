import collections
from typing import List
from collections import Counter
nums = [2, 3, 1, 3, 2]
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))

