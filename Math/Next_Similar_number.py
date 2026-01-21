class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        arr = list(A)
        n = len(arr)

        # Step 1: find first decreasing index
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i < 0:
            return "-1"

        # Step 2: find just larger digit on right
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1

        # Step 3: swap
        arr[i], arr[j] = arr[j], arr[i]

        # Step 4: sort right side
        arr[i + 1:] = sorted(arr[i + 1:])

        return ''.join(arr)
