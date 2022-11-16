##
# 给一个数组nums和目标值k，找到和等于k的最长子数组长度，如果不存在，返回0
"""
示例 1:
输入: nums = [1, -1, 5, -2, 3], k = 3

             0   1  2   3
输出: 4
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:
输入: nums = [-2, -1, 2, 1], k = 1
输出: 2
解释: 子数组 [-1, 2] 和等于 1，且长度最长。

"""
class Solution:
    def maxsubarray(self,nums, k):
        res = 0 ### 记录答案
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j]) == k:
                    res = max(res, j-i)
        return res
##dic 记录pre——sum
##{累价值:下标}
##pre_sum-k dic
dic{0:0}
##
if pre_sum - k in dic:
    res = max(res,i-dic[pre_sum - k])

if __name__ == '__main__':
    nums = [-2, -1, 2, 1]
    k = 1
    print(Solution().maxsubarray(nums,k))