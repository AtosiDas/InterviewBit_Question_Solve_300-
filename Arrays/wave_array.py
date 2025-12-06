class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
		B = sorted(A)
        i = 0
        while i < len(B) - 1:
            C = B[i]
            B[i] = B[i+1]
            B[i+1] = C
            i = i + 2
        return B
            