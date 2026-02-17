class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        firstRowZero = False
        firstColumnZero = False
        for i in range(n):
            if A[0][i] == 0:
                firstRowZero = True
        for j in range(m):
            if A[j][0] == 0:
                firstColumnZero = True
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0
        if firstRowZero:
            for i in range(n):
                A[0][i] = 0
        if firstColumnZero:
            for j in range(m):
                A[j][0] = 0
        return A