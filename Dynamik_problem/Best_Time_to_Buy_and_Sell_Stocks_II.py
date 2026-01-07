class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        profit = 0
        for i in range(0, len(A)-1):
            if A[i] < A[i+1]:
                profit += A[i+1] - A[i]
        return profit