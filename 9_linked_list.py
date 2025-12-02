# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        dummy = ListNode(0)
        dummy.next = A
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            
        return dummy.next