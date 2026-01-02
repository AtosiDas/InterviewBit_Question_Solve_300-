class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        arr = []
        st = ""
        for ch in A:
            if ch.islower():
                st += ch
            elif ch == '~':
                arr.append(st)
                st = ""
        return arr
            