# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result = ListNode()
        first = list1
        second = list2
        current = result

        while first or second:
            if first and not second:
                current.next = first
                first = first.next
            elif second and not first:
                current.next = second
                second = second.next
            elif first.val <= second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next

            current = current.next

        return result.next

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        result = lists[0]

        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])


        return result
