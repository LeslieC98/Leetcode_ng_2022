class LinkedList:
    def __init__(self, val):
        self._val = val
        self._next = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self,val):
        self._val = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self,n):
        self._next = n


def init_linked_list(l: list):
    head = LinkedList()
    current = head
    for i in l:
        current.val = i
        current.next = LinkedList()
        current = current.next
    return head


