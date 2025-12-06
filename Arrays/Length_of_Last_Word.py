class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
        count = 0
        last_word_length = 0
        for a in A:
            if a != ' ':
                count += 1
                last_word_length = count
            else:
                count = 0
        return last_word_length
                