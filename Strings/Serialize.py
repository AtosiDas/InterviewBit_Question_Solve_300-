class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):
        result = ""
        for a in A:
            result = result + a + str(len(a)) + '~'
        return result