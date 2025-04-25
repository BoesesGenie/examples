# https://leetcode.com/problems/reverse-nodes-in-k-group/

# NB: the algorithm can be optimized!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    result = ListNode()
    current = result

    def reverseKGroup(self, head, k):
        data = []
        pointer = head
        origin = head

        for i in range(k):
            if pointer is None:
                self.current.next = origin

                return

            data.append(pointer.val)
            pointer = pointer.next

        for i in range(k):
            value = data.pop(-1)
            self.current.next = ListNode(value)
            self.current = self.current.next

        self.reverseKGroup(pointer, k)

        return self.result.next
