class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2:
            return n

        write = 2  
        for read in range(2, n):
            if A[read] != A[write - 2]:
                A[write] = A[read]
                write += 1

        return write
