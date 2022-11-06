from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ##using sort function to sort the array
        intervals.sort(key = lambda x:x[0])
        merge = []
        for interval in intervals:
            ##[1,3] and [4,6]
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
            ## [1,3] and [2,6]
                merge[-1][1] = max(merge[-1][1], interval[1])
                ## 3                  3               6
        return merge


"""
time :O(nlog(n))
space:O(n)
interval = [2,6]
interval[0] = 2
1.merge = []
interval = [1,3]
merge[-1][1] ==0, <interval[0],append[1,3]
2.merge = [1,3]
interval = [2,6]
merge[-1][1] = 3, interval[0] = 2不append
merge[-1][1] = max(merged[-1][1], interval[1]) 
                    3             6
merge = [1,6]

"""