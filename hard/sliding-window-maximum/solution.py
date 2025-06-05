from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Tracks the current maximum value in the window
        current_max = nums[0]

        # Dictionary to store the frequency of elements within the window
        window_counts = {}

        # Final result list of max values from each window
        max_values = []

        for i in range(len(nums)):
            # Update the current max if the new element is greater
            if current_max < nums[i]:
                current_max = nums[i]

            # Add the current element to the frequency map
            window_counts[nums[i]] = window_counts.get(nums[i], 0) + 1

            # Once the window exceeds size k, remove the leftmost element
            if i >= k:
                outgoing_value = nums[i - k]
                window_counts[outgoing_value] -= 1

                # Remove from dict if count becomes zero
                if window_counts[outgoing_value] == 0:
                    del window_counts[outgoing_value]

                    # If the outgoing value was the current max, recalculate max
                    if current_max == outgoing_value:
                        current_max = max(window_counts.keys())

            # Start recording results once the first window is formed
            if i >= k - 1:
                max_values.append(current_max)

        return max_values


# ✅ Test cases
solution = Solution()
print(solution.maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3))  # ➤ [2, 2, 4, 4, 6]
print(solution.maxSlidingWindow([9, 5, 3, 1, 6, 3], 2))     # ➤ [9, 5, 3, 6, 6]
print(solution.maxSlidingWindow([4, 4, 4, 4], 2))           # ➤ [4, 4, 4]

"""
🧠 Time Complexity:
- In the worst case, we may need to recompute the max using `max(window_counts.keys())`, which takes O(k) time.
- So worst-case time complexity: O(n * k)

🧠 Space Complexity:
- Dictionary holds at most k unique elements → O(k)
- Result list holds (n - k + 1) elements → O(n)
- Total: O(k + n)
"""
