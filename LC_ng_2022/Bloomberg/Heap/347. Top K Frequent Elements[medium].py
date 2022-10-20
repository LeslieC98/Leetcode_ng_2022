from collections import Counter
import heapq
from typing import List


class Node:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.num > other.word
        return self.freq < other.freq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        heap = []
        for num, freq in dic.items():
            heapq.heappush(heap, (num, freq))
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)

        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(heap)[1]
        return res

if __name__ == '__main__':
    d1 =["2342349", "david", "m",3]
    d2 = [ "2342349", "Lee", "n", 4]
