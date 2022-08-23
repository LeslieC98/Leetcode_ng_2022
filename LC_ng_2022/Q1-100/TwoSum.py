from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, b in enumerate(nums):
            # a + b = target -> a = target - b
            a = target - b
            if a in hash:
                return [hash[a], i]
            hash[b] = i
