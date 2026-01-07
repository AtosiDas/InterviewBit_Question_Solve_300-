class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if not A:
            return 0

        dp = [A[0]]

        for i in range(1, len(A)):
            if A[i] > dp[-1]:
                dp.append(A[i])
            else:
                # find position to replace
                l, r = 0, len(dp) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if dp[mid] >= A[i]:
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[l] = A[i]

        return len(dp)
