class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        pos = 0
        neg = 0
        for a in A:
            if a > 0:
                pos += 1
            elif a < 0:
                neg += 1
        return [pos, neg]