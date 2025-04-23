# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        result = ListNode()
        current = result
        heap = []

        for node in lists:
            if not node:
                continue

            heapq.heappush(heap, (node.val, node))

        while heap:
            _, node = heapq.heappop(heap)

            current.next = node
            current = node

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return result.next
