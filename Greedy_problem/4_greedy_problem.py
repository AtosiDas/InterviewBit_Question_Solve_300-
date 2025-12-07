class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, A):
        A.sort()
        c1 = A[-1] * A[-2] * A[-3]
        c2 = A[0] * A[1] * A[-1]
        return max(c1, c2)
        

# Time complexity: O(nlogn)
# Space Complexity: O(1)