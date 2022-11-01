from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ##heap initialization
        free_room = []
        ##sort the meetings in increasing order of their start time