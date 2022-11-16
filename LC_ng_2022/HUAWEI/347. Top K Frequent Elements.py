import collections
from collections import Counter

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap = []
        ##数据堆入
        for num, freq in dic.items():
            
            heapq.heappush(heap, (freq,num))
            print(heap)
            if len(heap) > k: ##长度大于k，pop最小
                heapq.heappop(heap)
        return [i[1] for i in heap]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums,k))