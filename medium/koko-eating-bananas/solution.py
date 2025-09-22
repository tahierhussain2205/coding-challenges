from typing import List
import math


class Solution:
    def minEatingSpeed(self, banana_piles: List[int], available_hours: int) -> int:
        # Binary search between 1 and the largest pile
        min_speed, max_speed = 1, max(banana_piles)
        optimal_speed = max_speed

        while min_speed <= max_speed:
            current_speed = (min_speed + max_speed) // 2

            # Calculate total hours needed at current eating speed
            total_hours_needed = 0
            for pile_size in banana_piles:
                total_hours_needed += math.ceil(pile_size / current_speed)

            # If we can finish within the time limit, try a slower speed
            if total_hours_needed <= available_hours:
                optimal_speed = min(optimal_speed, current_speed)
                max_speed = current_speed - 1
            else:
                # Need to eat faster
                min_speed = current_speed + 1

        return optimal_speed


# Test cases
solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # Expected: 4
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Expected: 30

# Time Complexity: O(n * log(max(piles))) where n is the number of piles
# - Binary search runs in O(log(max(piles))) iterations
# - Each iteration calculates hours for all piles in O(n) time

# Space Complexity: O(1)
# - Only using constant extra space for variables

# Algorithm: Binary search to find minimum eating speed
# 1. Set search range from 1 to max pile size
# 2. For each candidate speed, calculate total hours needed
# 3. If feasible (≤ h hours), try slower speed; otherwise try faster speed
# 4. Return the minimum feasible speed found
