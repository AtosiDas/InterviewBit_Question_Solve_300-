class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        arr = []
        
        if A == 0:
            return arr
        else:
            for i in range(A):
                row = [0] * (i + 1)
                row[0] = 1
                row[i] = 1
                for j in range(1, i):
                    row[j] = arr[i-1][j] + arr[i-1][j-1]
                arr.append(row)
            return arr
            