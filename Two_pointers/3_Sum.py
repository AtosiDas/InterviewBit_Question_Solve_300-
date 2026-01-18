class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        closet_sum = A[0] + A[1] + A[2]
        for i in range(0, len(A)-2):
            l = i + 1
            r = len(A) - 1
            while l < r:
                current_sum = A[i] + A[l] + A[r]
                if abs(current_sum - B) < abs(closet_sum - B):
                    closet_sum = current_sum
                if current_sum > B:
                    r -= 1
                elif current_sum < B:
                    l += 1
                else:
                    return current_sum            
        return closet_sum