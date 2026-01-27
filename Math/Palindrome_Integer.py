class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        if A < 0:
            return 0
        B = 0
        C = A
        while A > 0:
            rem = A % 10
            B = B * 10 + rem
            A = A // 10
        if C == B:
            return 1
        return 0