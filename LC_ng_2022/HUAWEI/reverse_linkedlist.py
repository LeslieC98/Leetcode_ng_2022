
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self,val):
        self.val = None
        self.next = None

class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        nex = None
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        print(head)
        return pre

if __name__ == '__main__':

    head= ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    head.next = node_2
    node_2.next = node_3
    print(Solution().ReverseList(head))

