from random import choice


class RandomizedSet:

    def __init__(self):
        self.nums = [] ##nums 存放数字
        self.value_index= {} ##存放数字在nums中对应的下标，num => index


    def insert(self, val: int) -> bool:
        ##在变长数组的末尾添加val
        if val in self.value_index:
            return False
        ##在添加wal之前的变长数组长度为val所在下标index， 将val和下标inder存入哈希表；
        self.value_index[val] = len(self.nums)
        self.nums.append(val)
        ##返回true
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_index:
            return False
        ##从哈希表中获得val的下标index
        id = self.value_index[val]
        ##从哈希表中获得val的下标index移动到下标index处，在哈希表中将last的下标更新为index
        self.nums[id] = self.nums[-1]
        self.value_index[self.nums[id]] = id
        ##在变长数组中删除最后一个元素，在哈希表中删除val
        self.nums.pop()
        del self.value_index[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)