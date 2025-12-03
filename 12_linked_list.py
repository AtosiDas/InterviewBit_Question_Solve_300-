# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        temp = A
        zeros = 0
        ones = 0
        while temp:
            if temp.val == 0:
                zeros += 1
            else:
                ones += 1
            temp = temp.next
        temp = A
        for _ in range(zeros):
            temp.val = 0
            temp = temp.next
        for _ in range(ones):
            temp.val = 1
            temp = temp.next
        return A