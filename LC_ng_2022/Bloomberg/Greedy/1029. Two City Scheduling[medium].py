from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        print(costs)
        mid = len(costs) // 2
        res = 0
        for i in range(mid):
            res += costs[i][1]
        for j in range(mid, len(costs)):
            res += costs[j][0]

        return res

"""
时间复杂度：O(nlogN)
space :O(1)
"""