class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        words = A.split()
        words.reverse()
        return " ".join(words)