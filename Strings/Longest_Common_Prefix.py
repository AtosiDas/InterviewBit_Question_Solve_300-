class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ""

        # Step 1: find length of shortest string
        mini = len(A[0])
        for s in A:
            mini = min(mini, len(s))

        prefix = ""

        # Step 2: compare character by character
        for i in range(mini):
            ch = A[0][i]
            for s in A:
                if s[i] != ch:
                    return prefix
            prefix += ch

        return prefix