class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
        def isPrime(a: str):
            for i in range(2, a // 2):
                if a % i == 0:
                    return False
            return True
        i = 2
        for i in range(2, A // 2 + 1):
            if isPrime(i) and isPrime(A - i):
                return [i, A - i]