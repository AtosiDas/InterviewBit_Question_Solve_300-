# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        # C must start as a dummy node so you can append to it
        C = ListNode(0)
        temp = C

        # Loop while both lists have nodes
        while A and B:
            if A.val <= B.val:
                temp.next = ListNode(A.val)
                temp = temp.next
                A = A.next
            else:
                temp.next = ListNode(B.val)
                temp = temp.next
                B = B.next

        # Append remaining nodes from A
        while A:
            temp.next = ListNode(A.val)
            temp = temp.next
            A = A.next

        # Append remaining nodes from B
        while B:
            temp.next = ListNode(B.val)
            temp = temp.next
            B = B.next

        # Return the merged list head
        return C.next
