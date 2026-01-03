class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        while i < len(A):
            result.append(A[i])
            i += 1
        while j < len(B):
            result.append(B[j])
            j += 1
        A.clear()
        A.extend(result)