class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        arr = []
        parts = A.split(",")
        for a in parts:
            arr.append(int(a))
        return arr