class Solution:
    def solve(self, A):
        mod = 10**9 + 7
        n = len(A)

        left = [1] * n
        right = [1] * n

        # Prefix product
        for i in range(1, n):
            left[i] = (left[i-1] * A[i-1]) % mod

        # Suffix product
        for i in range(n-2, -1, -1):
            right[i] = (right[i+1] * A[i+1]) % mod

        # Result
        result = []
        for i in range(n):
            result.append((left[i] * right[i]) % mod)

        return result