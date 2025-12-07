class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        if A == 1:
            return 1
        elif A == 2:
            return 2
        return self.climbStairs(A-1) + self.climbStairs( A-2)