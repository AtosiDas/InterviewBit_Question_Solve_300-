class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		seen = set()
		for a in A:
            if a + B in seen or a - B in seen:
                return 1
            seen.add(a)
        return 0

# The time complexity is O(n)


# class Solution:
# 	# @param A : list of integers
# 	# @param B : integer
# 	# @return an integer
# 	def diffPossible(self, A, B):
# 		for i in range(len(A)-1):
# 			for j in range(i + 1, len(A)):
# 				if abs(A[i] - A[j]) == B:
# 					return 1		
#         return 0



# ✅ Correct logic is not enough
# ✅ Always estimate time complexity
# ❌ O(n²) is almost always rejected for large inputs