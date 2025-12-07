class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        return max(abs(a - b) for a, b in zip(A_sorted, B_sorted))
	

# Time Complexity : O(nlongn)
# Space Complexity: O(n)