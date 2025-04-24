# https://leetcode.com/problems/swap-nodes-in-pairs/

# maybe needs more elegant solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    result = ListNode()
    current = result

    def swapPairs(self, head):
        if head is None:
            return None

        if head.next is None:
            self.current.next = head

            return self.result.next

        self.current.next = ListNode(head.next.val)
        self.current = self.current.next
        self.current.next = ListNode(head.val)
        self.current = self.current.next

        if head.next.next:
            self.swapPairs(head.next.next)

        return self.result.next
