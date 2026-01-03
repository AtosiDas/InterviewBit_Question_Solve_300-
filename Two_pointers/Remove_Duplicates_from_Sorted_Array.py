class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        for j in range(1, len(A)):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]
        return i+1
            