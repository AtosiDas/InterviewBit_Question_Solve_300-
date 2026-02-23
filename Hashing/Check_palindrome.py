class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = {}
        for a in A:
            if a in count:
                count[a] += 1
            else:
                count[a] = 1
        total = 0
        for key, value in count.items():
            if count[key] % 2 == 1:
                total += 1
        if total > 1:
            return 0
        return 1