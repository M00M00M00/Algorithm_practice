from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = 0
        cnt = 1
        while l1:
            a1 += cnt * l1.val
            cnt += 1
            l1 = l1.next
        cnt = 1
        a2 = 0
        while l2:
            a2 += cnt * l2.val
            cnt += 1
            l2 = l2.next
        answer = a1 + a2
        while answer > 0:
            l3 = lis

