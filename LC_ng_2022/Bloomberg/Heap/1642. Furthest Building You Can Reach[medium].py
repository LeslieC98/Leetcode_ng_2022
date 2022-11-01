
from typing import List    # 类型注解的建议
import heapq


class Solution:
    # lc 1642. 可以到达的最远建筑
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heapq方法，先用砖头，当不够用时用梯子，替换已用最大的砖头    120 ms
        # 小根堆heapq由小到大，pop时小的先出；而sort是由小到大，pop时大的先出
        hq = []
        length = len(heights)
        if length < 2:
            return 0
        for h in range(1, length):
            diff = heights[h] - heights[h - 1]
            if diff > 0:    # 下层建筑高，才需要借外物攀爬；否则直接跳到下一个建筑
                heapq.heappush(hq, -diff)    # 通过负数模拟最大堆
                bricks -= diff    # 试着先用砖头
                if bricks < 0:
                    if ladders > 0:    # 砖头本次不够用，梯子还有
                        ladders -= 1    # 用新梯子换已用的最大砖头
                        bricks += -heapq.heappop(hq)    # 砖头再补充已用的最大的砖头，如果是本次的砖头最大也可以换成梯子
                    else:
                        return h - 1
        return h
