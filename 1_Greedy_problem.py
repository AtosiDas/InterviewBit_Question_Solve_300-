class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = 0
        candidate = None
        for x in A:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
# Time Complexity O(N)
# Space Complexity O(1)


# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def majorityElement(self, A):
#         if len(A) == 1:
#             return A[0]
#         B = list(A)
#         B.sort()
#         return B[len(B) // 2]

# Time Complexity O(NlogN)
# Space Complexity O(N)