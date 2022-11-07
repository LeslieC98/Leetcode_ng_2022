# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


def ListNode(digit):
    pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ##carry就是进位的意思
        ##Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.
        # Initialize carry to 0
        carry = 0
        ##we use dummy to avoid special situation
        cur = dummy = ListNode(0)
        ##Loop through lists l1 and l2 until you reach both ends and carry is 0.
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            ##取余数：Take the remainder of digit 9+9/10 =8
            digit = (d1 + d2 + carry) % 10
            ##取整数：Take an integer for carry 9+9/10 =1
            carry = (d1 + d2 + carry) // 10
            cur.next = ListNode(digit)
            cur = cur.next
            ##推进当前节点至下一个节点。advance current node to next.
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next
    ###O(n) O(n)