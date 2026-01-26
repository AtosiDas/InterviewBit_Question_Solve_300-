class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        rev = 0
        B = abs(A)
        while B > 0:
            rem = B % 10
            rev = (rev * 10) + rem
            B = B // 10
        if rev < -(2**31) or rev > (2**31) - 1:
            return 0
        if A > 0:
            return rev
        else:
            return -rev