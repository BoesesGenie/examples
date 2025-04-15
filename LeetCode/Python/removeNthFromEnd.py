# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        as_list = []

        while current.next is not None:
            as_list.append(current)
            current = current.next

        as_list.append(current)

        index = len(as_list) - n
        prev_index = index - 1
        next_index = index + 1

        if prev_index >= 0 and next_index < len(as_list):
            as_list[prev_index].next = as_list[next_index]

            return head

        if prev_index == -1 and next_index < len(as_list):
            return as_list[next_index]

        if prev_index >= 0 and next_index == len(as_list):
            as_list[prev_index].next = None

            return head
