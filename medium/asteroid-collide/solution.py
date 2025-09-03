from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate asteroid collisions using a stack-based approach.

        Algorithm:
        1. Use a stack to track surviving asteroids as we process from left to right
        2. For each new asteroid, check if it collides with the top of the stack
        3. Collision occurs when: right-moving asteroid (positive) meets left-moving asteroid (negative)
        4. Resolve collisions based on size comparison until no more collisions occur
        5. Add surviving asteroid to stack

        Collision rules:
        - Smaller asteroid explodes, larger survives
        - Equal size asteroids both explode
        - Same direction asteroids never collide
        """
        # Stack to maintain asteroids that survive collisions
        surviving_asteroids = []

        for current_asteroid in asteroids:
            # If stack is empty, add asteroid directly
            if len(surviving_asteroids) == 0:
                surviving_asteroids.append(current_asteroid)
                continue

            # No collision cases:
            # 1. Previous asteroid moving left (negative) - no collision possible
            # 2. Both asteroids moving right (positive) - no collision
            if surviving_asteroids[-1] < 0 or (surviving_asteroids[-1] > 0 and current_asteroid > 0):
                surviving_asteroids.append(current_asteroid)
                continue

            # Potential collision: right-moving meets left-moving asteroid
            # Process all possible collisions with current asteroid
            remaining_asteroid = None

            while len(surviving_asteroids) > 0:
                remaining_asteroid = None
                current_size = abs(current_asteroid)

                # Check if collision is possible (different directions)
                if current_asteroid < 0 and surviving_asteroids[-1] < 0 or current_asteroid > 0 and surviving_asteroids[-1] > 0:
                    surviving_asteroids.append(current_asteroid)
                    break

                # Current asteroid is smaller - it gets destroyed
                if current_size < surviving_asteroids[-1]:
                    break

                # Equal size - both asteroids destroyed
                if current_size == surviving_asteroids[-1]:
                    surviving_asteroids.pop()
                    break

                # Current asteroid is larger - destroy the previous one
                surviving_asteroids.pop()
                remaining_asteroid = current_asteroid

            # If all previous asteroids were destroyed and current survives, add it
            if len(surviving_asteroids) == 0 and remaining_asteroid:
                surviving_asteroids.append(remaining_asteroid)

        return surviving_asteroids


solution = Solution()

# Test Case 1: Mixed collisions with survivors
test1 = [10, 2, -5]
result1 = solution.asteroidCollision(test1)
print(f"Input: {test1}")
print(f"Output: {result1}")
print(f"Expected: [10]")
print(f"Correct: {result1 == [10]}")
print("Explanation: 2 and -5 collide -> -5 wins, then 10 and -5 collide -> 10 wins")
print()

# Test Case 2: Complete mutual destruction
test2 = [8, -8]
result2 = solution.asteroidCollision(test2)
print(f"Input: {test2}")
print(f"Output: {result2}")
print(f"Expected: []")
print(f"Correct: {result2 == []}")
print("Explanation: 8 and -8 have equal size, both explode")


"""
COMPLEXITY ANALYSIS:

Time Complexity: O(n)
- We iterate through each asteroid once: O(n)
- Each asteroid can be pushed to and popped from the stack at most once
- Total stack operations across all asteroids: O(n)
- Overall: O(n) where n is the number of asteroids

Space Complexity: O(n)
- In the worst case, no collisions occur and all asteroids survive
- Stack can hold up to n asteroids
- Overall: O(n) for the surviving_asteroids stack

ALGORITHM WALKTHROUGH:
This solution uses a stack to simulate the collision process:

1. PROCESSING: Iterate through asteroids from left to right (order matters)
2. NO COLLISION CASES:
   - Empty stack: Add asteroid directly
   - Previous asteroid moving left (negative): No collision possible
   - Both asteroids moving right (positive): No collision possible
3. COLLISION RESOLUTION:
   - Only occurs when right-moving meets left-moving asteroid
   - Use while loop to handle chain reactions (one collision can trigger more)
   - Compare absolute values to determine winner
   - Equal sizes result in mutual destruction
"""
