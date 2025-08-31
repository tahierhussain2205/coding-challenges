from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs for easier processing
        position_speed_pairs = list(zip(position, speed))

        # Stack to track distinct car fleets (stores time to reach target)
        fleet_times = []
        
        # Process cars starting from those closest to target (reverse sorted by position)
        for car_position, car_speed in sorted(position_speed_pairs)[::-1]:
            # Calculate time for this car to reach target
            time_to_target = (target - car_position) / car_speed
            fleet_times.append(time_to_target)

            # If current car takes less or equal time than the car ahead,
            # it will catch up and form a fleet with the slower car
            if len(fleet_times) > 1 and fleet_times[-1] <= fleet_times[-2]:
                fleet_times.pop()  # Merge into existing fleet (remove faster car's time)

        # Number of remaining times in stack = number of distinct fleets
        return len(fleet_times)


# Test cases
solution = Solution()

print("Test case 1:")
print("Target: 12, Position: [10,8,0,5,3], Speed: [2,4,1,1,3]")
print("Expected: 3, Got:", solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

print("\nTest case 2:")
print("Target: 10, Position: [3], Speed: [3]")
print("Expected: 1, Got:", solution.carFleet(10, [3], [3]))

"""
Time Complexity Analysis:
- O(n log n) due to sorting the position-speed pairs by position
- The subsequent loop through sorted pairs is O(n)
- Overall: O(n log n)

Space Complexity Analysis:
- O(n) for storing the position_speed_pairs list
- O(n) for the fleet_times stack in worst case (when no cars form fleets)
- Overall: O(n)

Algorithm Explanation:
1. Sort cars by position (closest to target first)
2. For each car, calculate time to reach target
3. If a car behind takes ≤ time than car ahead, they form a fleet
4. Use stack to track distinct fleet times - merge fleets by removing faster times
5. Final stack size = number of car fleets
"""
