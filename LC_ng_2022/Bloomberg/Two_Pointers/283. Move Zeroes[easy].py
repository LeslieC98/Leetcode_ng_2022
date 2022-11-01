from typing import List

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0,0
        while right < n:
            if nums[right] != 0:
                while left < right and nums[left] != 0:
                    left += 1
                nums[left] ,nums[right] = nums[right], nums[left]
            right += 1
        return nums

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast, slow = 0,0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        return nums

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))

##O(n) traversed the entire array

## O(1) modify nums in-place instead.
