class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        gt = 0
        lt = 0
        for i in range(len(A)):
            if A[i] > C:
                gt += 1
        for j in range(len(B)):
            if B[j] < C:
                lt += 1
        if gt > lt:
            return gt
        else:
            return lt