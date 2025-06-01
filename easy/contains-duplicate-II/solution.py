from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        last_seen_index = {}

        # Iterate over the list
        for current_index in range(len(nums)):
            num = nums[current_index]

            # If the number was seen before
            if num in last_seen_index:
                # Check if the previous occurrence is within distance k
                if abs(current_index - last_seen_index[num]) <= k:
                    return True  # Found a nearby duplicate
                # Update the last seen index
                last_seen_index[num] = current_index
            else:
                # Store the index of the first occurrence
                last_seen_index[num] = current_index

        # No nearby duplicates found
        return False


# Test cases
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(solution.containsNearbyDuplicate([2, 1, 2], 1))     # Output: False


"""
Time Complexity: O(n)
- We iterate over the list once.
- Dictionary operations (lookup and update) are O(1) on average.
- So overall time is linear with respect to the number of elements.

Space Complexity: O(min(n, k))
- In the worst case, we store up to k+1 unique elements in the dictionary.
- So the space usage is proportional to the sliding window size.
"""
