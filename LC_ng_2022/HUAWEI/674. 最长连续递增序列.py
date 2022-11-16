from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录 nums[i+1] = 3> nums[i] = 1
                dp[i+1] = dp[i] + 1 ###dp = [1,2,1,1,1]
            result = max(result, dp[i+1])
        return result

if __name__ == '__main__':
    nums = [1,3,5,4,7]
    print(Solution().findLengthOfLCIS(nums))
