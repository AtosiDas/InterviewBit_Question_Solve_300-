class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        max_so_far = float('-inf')
        for a in A:
            if a > max_so_far:
                count += 1
                max_so_far = a
        return count