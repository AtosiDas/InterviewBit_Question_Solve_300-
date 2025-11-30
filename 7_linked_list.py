# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        # handle empty list
        if A is None:
            return None

        current = A
        while current and current.next:
            if current.val == current.next.val:
                # skip the duplicate node
                current.next = current.next.next
            else:
                # move forward only when next is different
                current = current.next
        return A
