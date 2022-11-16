""""



题目8：
给你一个数组，按照数组中数组重复个数从多到少排序输出,重复个数相同按照数值从小到大排序。

示例 ：
输入：[2,3,8,5,7,5,7,6,9,1,6,6]
输出：[6,6,6,5,5,7,7,1,2,3,8,9]

输入：[99999999999,8,7,6,5,4,3,2,1,0,0]
输出：[0,0,1,2,3,4,5,6,7,8,99999999999]

"""
import collections


class Solution:
    def sort_list(self,nums):
        dic = collections.Counter(nums) ##dic ({6: 3, 5: 2, 7: 2, 2: 1, 3: 1, 8: 1, 9: 1, 1: 1})
        list_sort = sorted(dic.items(), key = lambda x:(-x[1],x[0]))
        res = []
        for i in list_sort:
            for j in range(i[1]):
                res.append(i[0])


        return res



if __name__ == '__main__':
    nums_2 = [99999999999,8,7,6,5,4,3,2,1,0,0]
    nums_1 = [2,3,8,5,7,5,7,6,9,1,6,6]
    print(Solution().sort_list(nums_1))
    print(Solution().sort_list(nums_2))





