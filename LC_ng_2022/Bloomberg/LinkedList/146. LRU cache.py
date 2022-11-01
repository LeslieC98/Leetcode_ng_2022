
class ListNode:
    def __init__(self,key = 0, val = 0): ##defind double linekd List
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head =ListNode() ##create empty linkedlist
        self.tail = ListNode()
        self.head.next= self.tail
        self.tail.prev = self.head

    def remove_node(self,node):
        node.prev.next = node.next##先后再前
        node.next.prev = node.prev



    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
