# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        currentResult = l3
        carry = 0

        while l1 or l2 or carry > 0:
            currentL1Val = l1 and l1.val or 0
            currentL2Val = l2 and l2.val or 0

            print(currentL1Val)
            print(currentL2Val)

            sum = currentL1Val + currentL2Val + carry
            currentResult.next = ListNode(sum % 10)
            currentResult = currentResult.next

            carry = math.floor(sum / 10)
            l1 = l1 and l1.next or None
            l2 = l2 and l2.next or None

        print(l3.next)
        return l3.next
