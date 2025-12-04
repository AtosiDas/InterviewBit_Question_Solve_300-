class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        arr = [1]
        if A == 0:
            return arr
        elif A == 1:
            arr.append(1)
            return arr
        else:
            for _ in range(A):
                arr.append(1)
                for i in range(len(arr) - 2, 0, -1):
                    arr[i] = arr[i] + arr[i - 1]
            return arr    