from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n+1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream##把self.stream赋给stream,前面是类属性，后面是局部变量


        stream_[idKey] = value
        res = list()
        while self.ptr < len(stream_) and stream_[self.ptr]:##不为空且指针未超过边界，append
            res.append(stream_[self.ptr])
            self.ptr += 1

        return res
