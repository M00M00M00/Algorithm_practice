from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = ""
        while l1:
            a1 += str(l1.val)
            l1 = l1.next
        a2 = ""
        while l2:
            a2 += str(l2.val)
            l2 = l2.next
        answer = str(int(a1[::-1]) + int(a2[::-1]))
        

