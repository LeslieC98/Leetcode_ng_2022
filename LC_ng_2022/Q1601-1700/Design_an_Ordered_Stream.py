from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = valuegi
        ans = []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans


def run(l1: List[str], l2: List[List]):
    ans = []
    l1.pop(0)
    n = l2.pop(0)[0]
    stream = OrderedStream(n) ##初始化OrderStream
    ans.append('null')
    for i in range(len(l1)):
        if l1[i] == "insert":
            ans.append(stream.insert(*l2[i]))
    print(ans)


if __name__ == '__main__':
    run(["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
        [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]])
