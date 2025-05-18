from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0           # Points to the current left boundary
        right = 0          # Scans to find a right boundary
        trapped_water = 0  # Accumulates total trapped water

        # Loop through the elevation map until the right pointer reaches the end
        while right < n:
            right += 1  # Move the right pointer one step ahead

            # As long as the height at right is less than the height at left,
            # we assume water can be trapped between left and right
            while right < n and height[left] > height[right]:
                trapped_water += height[left] - height[right]
                right += 1

            # If no valid right boundary was found (i.e., array ended)
            if right == n:
                right -= 1  # Step back to the last valid index
                backtrack = right

                # Now try to find the next highest left boundary from the right side
                while backtrack > left:
                    backtrack -= 1

                    # Skip over bars that are shorter than or equal to current bar
                    while backtrack > left and height[backtrack] <= height[right]:
                        backtrack -= 1

                    # We've overcounted the area (assuming left boundary was too high),
                    # so we subtract the extra area between right and new left
                    overcounted = (right - backtrack) * (height[left] - height[right])
                    trapped_water -= overcounted

                    # Move right pointer to backtrack position and repeat if needed
                    right = backtrack

                break  # Exit the main loop as the end of the array has been reached

            # If a valid right boundary was found, move left to the new right
            if right > left:
                left = right

        return trapped_water


# ✅ Test cases
solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
print(solution.trap([5, 4, 1, 2]))                         # Output: 1
print(solution.trap([4, 2, 0, 3, 2, 5]))                   # Output: 9
print(solution.trap([1, 2, 3, 4, 5]))                      # Output: 0
print(solution.trap([5, 4, 3, 2, 1]))                      # Output: 0

"""
Time Complexity: O(n)
- Each index is visited at most twice (once in forward scan, possibly again in backtrack).
- Hence, total time is linear in size of input.

Space Complexity: O(1)
- Only scalar variables are used, no extra space proportional to input.
"""
