"""
满足和大于等于 target 的最小连续子数组的长度。
输入：target = 7, nums = [2,3,1,2,4,3]  输出：2

"""
class Solution:
    def longestarray(self, nums, target):
        ##首先list是无序的而不是有序的，所以排binary search，然后因为输出的结果是连续数组的长度，所以用sliding windiows
        tmp = 0 ##窗口和
        left, right = 0, 0 ##指针移动
        res = len(nums) ##结果 --数组长度
       ## [2, 3, 1, 2, 4, 3]
       ##  l
       ##  r
       ## res = 6
        while right < len(nums): ## 0 < 6
            tmp += nums[right] ##tmp = 2
            ##调整窗口大小
            while tmp >= target: ##2<target
                res = min(len(nums), right - left +1)
                tmp -= nums[left]
                left += 1
            right += 1 ##right = 1
        return res
if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(Solution().longestarray(nums,target))
