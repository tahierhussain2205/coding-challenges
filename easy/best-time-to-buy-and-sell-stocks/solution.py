from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_days = len(prices)

        # Edge case: Not enough data to perform a buy/sell operation
        if num_days <= 1:
            return 0

        # Initialize the index of the lowest price seen so far (potential buying day)
        buy_day_index = 0
        max_profit = 0

        # Start from day 1 since day 0 is the initial buying candidate
        for sell_day_index in range(1, num_days):
            # If selling today would yield profit, calculate and update max profit
            if prices[sell_day_index] > prices[buy_day_index]:
                current_profit = prices[sell_day_index] - prices[buy_day_index]
                max_profit = max(max_profit, current_profit)
            # If today's price is lower than our current buy candidate, update buy_day_index
            elif prices[sell_day_index] < prices[buy_day_index]:
                buy_day_index = sell_day_index

        return max_profit


# Example usage
solution = Solution()

# Test Case 1: Buy on day 1 (price=1), sell on day 4 (price=6)
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5

# Test Case 2: Buy on day 1 (price=1), sell on day 4 (price=7)
print(solution.maxProfit([10, 1, 5, 6, 7, 1]))  # Output: 6

"""
Time Complexity: O(n)
- We traverse the prices list only once, comparing each day's price to the current minimum.
- All operations inside the loop are constant time.

Space Complexity: O(1)
- We use only a few variables (integers), regardless of the size of the input list.
"""
