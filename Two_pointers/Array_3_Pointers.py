class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i = 0
        j = 0
        k = 0
        
        # If any of the arrays are empty (not likely given the constraints, but for safety)
        if not A or not B or not C:
            return 0
        
        maxi = float('inf')
        
        # While all pointers are within bounds
        while i < len(A) and j < len(B) and k < len(C):
            # If all three values are the same, we can return 0 immediately
            if A[i] == B[j] == C[k]:
                return 0
            
            # Find the minimum and maximum among A[i], B[j], C[k]
            mini = min(A[i], B[j], C[k])
            current_max = max(A[i], B[j], C[k]) - mini
            maxi = min(current_max, maxi)
            
            # Increment the pointer for the array that contains the minimum element
            if mini == A[i]:
                i += 1
            elif mini == B[j]:
                j += 1
            else:
                k += 1
        
        return maxi
 