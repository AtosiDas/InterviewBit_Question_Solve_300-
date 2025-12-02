# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        lengthOfList = 0
        while temp:
            lengthOfList += 1
            temp = temp.next
        count = lengthOfList - B
        if count <= 0:
            return A.next
        else:
            prev = A
            for i in range(0, count-1):
                prev = prev.next    
            prev.next = prev.next.next
        return A