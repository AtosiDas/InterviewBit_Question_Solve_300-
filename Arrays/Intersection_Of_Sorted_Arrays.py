class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
        arr = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
               arr.append(A[i])
               i += 1
               j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return arr 
     
# Time Complexity: O(n + m) where n  = length of A, m =  length of B
# Space Complexity: O(k), k is the length of intersection array