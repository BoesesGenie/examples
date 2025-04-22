# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        lists = filter(lambda i: not i is None, lists)

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        result = ListNode()
        current = result

        while len(lists):
            min_index = 0
            min_value = lists[0].val

            for i in range(1, len(lists)):
                if min_value >= lists[i].val:
                    min_index = i
                    min_value = lists[i].val

            current.next = lists[min_index]
            current = current.next

            if lists[min_index].next is None:
                lists.pop(min_index)
            else:
                lists[min_index] = lists[min_index].next

        return result.next
