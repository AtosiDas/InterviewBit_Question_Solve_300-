class Solution:
    # @param A : tuple/list of integers
    # @return an integer
    def maxProfit(self, A):
        # handle empty or single-element inputs
        if not A or len(A) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in A:
            if price < min_price:
                min_price = price
            else:
                # possible profit if we sell today
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
