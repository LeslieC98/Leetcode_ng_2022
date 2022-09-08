from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.user = {}  ##{id: [stationName, t]}，记录每个乘客的{stationName,t}
        self.time = defaultdict(list)  ## # 字典：{(start_station, end_station): [total_time, count]}，记录每对站点的总时间和出现次数

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.user[id][0]
        total_time = t - self.user[id][1]  ##why 1
        # 该(始发站, 终点站)不在字典中，则增加这一项，初始化value值
        if (start_station, stationName) not in self.time:
            self.time.setdefault((start_station, stationName), [total_time, 1])
        # 在字典中，更新value值
        else:
            self.time[(start_station, stationName)][0] += total_time
            self.time[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation, endStation)][0] / self.time[(startStation, endStation)][1]
