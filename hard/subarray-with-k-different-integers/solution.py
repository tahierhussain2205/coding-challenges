from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        valid_subarrays_count = 0
        n = len(nums)

        # Loop through each possible starting index of the subarray
        for start in range(n - k + 1):
            # Initialize a set with the first k elements from the current starting index
            distinct_elements = set(nums[start: start + k])
            unique_count = len(distinct_elements)

            # If the initial subarray has exactly k distinct integers, count it
            if unique_count == k:
                valid_subarrays_count += 1

            # Expand the subarray to the right, starting just after the initial k-length window
            for end in range(start + k, n):
                # Add the new element only if it's not already in the set
                if nums[end] not in distinct_elements:
                    distinct_elements.add(nums[end])
                    unique_count += 1

                # If the number of unique elements exceeds k, break early
                if unique_count > k:
                    break

                # If we still have exactly k unique elements, count this subarray
                if unique_count == k:
                    valid_subarrays_count += 1

        return valid_subarrays_count


# ✅ Test cases
solution = Solution()
print(solution.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))  # Expected: 7
print(solution.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))  # Expected: 3
print(solution.subarraysWithKDistinct(nums=[1, 2, 3, 4, 5], k=1))  # Expected: 5

"""
Time Complexity:
- Outer loop runs O(n)
- Inner loop (in worst case) can run O(n) for each start index
- Set operations (add, lookup) are O(1) on average
=> Overall Time Complexity: O(n^2)

Space Complexity:
- Each subarray uses a set that can hold up to k elements
=> Overall Space Complexity: O(k)
"""
