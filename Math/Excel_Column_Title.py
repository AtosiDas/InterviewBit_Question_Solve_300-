class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
        result = ""
        while A > 0:
            rem = (A % 26)
            if rem == 0:
                rem = 26
                A = (A // 26) - 1
            else:
                A = A // 26
            result += chr(ord('A') + rem - 1)
        return result[::-1]