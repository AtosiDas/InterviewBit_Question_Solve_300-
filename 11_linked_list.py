# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp = A
        N = 0
        while temp:
            N += 1
            temp = temp.next
        mid = N // 2 + 1
        value = mid - B
        if value <= 0:
            return -1
        else:
            for _ in range(value - 1):
                A = A.next
            return A.val