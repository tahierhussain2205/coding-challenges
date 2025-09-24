from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search bounds: minimum capacity must be the heaviest package,
        # maximum capacity is the sum of all packages (ship everything in one day)
        min_capacity = max(weights)
        max_capacity = sum(weights)

        result = max_capacity
        while min_capacity <= max_capacity:
            ship_capacity = (min_capacity + max_capacity) // 2

            # Calculate how many days needed with this capacity
            required_days = 1
            current_load = 0
            for package_weight in weights:
                current_load += package_weight
                if current_load > ship_capacity:
                    # Need a new day for this package
                    current_load = package_weight
                    required_days += 1

            if required_days <= days and ship_capacity < result:
                result = ship_capacity

            # Binary search: if we can ship within the days limit, try smaller capacity
            if required_days <= days:
                max_capacity = ship_capacity - 1
            else:
                min_capacity = ship_capacity + 1

        return result


# Test cases
solution = Solution()
print(solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # Expected: 15
print(solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3))  # Expected: 6

# Time Complexity: O(n * log(sum - max)) where n is the number of packages
# - Binary search runs in O(log(sum - max)) iterations
# - Each iteration requires O(n) time to simulate the shipping process
# Space Complexity: O(1) - only using constant extra space for variables
#
# Algorithm: Binary search on the ship capacity
# 1. Set bounds: minimum = heaviest package, maximum = sum of all packages
# 2. For each mid capacity, simulate shipping to count required days
# 3. If we can ship within the day limit, try smaller capacity (search left)
# 4. Otherwise, we need larger capacity (search right)
