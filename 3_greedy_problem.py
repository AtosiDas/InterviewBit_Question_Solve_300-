class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        flip = 0
        count = 0
        for a in A:
            effective = a ^ (flip % 2)
            if effective == 0:
                count += 1
                flip += 1
        return count


# Time Complexity: O(n)
# Space Complexity: O(1)





# class Solution:
# 	# @param A : list of integers
# 	# @return an integer
# 	def bulbs(self, A):
# 		count = 0
# 		I = [1] * len(A)
# 		for i in range(len(A)):
# 			if A[i] == 0:
# 				count += 1
# 				for j in range(i, len(A)):
#                     A[j] = 1 - A[j]
# 		return count 



# TestCase - Hard  Failed
# Time Limit Exceeded.
# In an actual interview, the sooner you arrive at the most optimal solution, the better. In general, try to correctly estimate the time complexity of your solution.
