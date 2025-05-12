from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: if the array is empty or has one element
        if len(nums) <= 1:
            return len(nums)

        # Convert the list to a set for O(1) lookups and deletions
        remaining_nums = set(nums)
        total_elements = len(nums)
        max_sequence_length = 1

        while remaining_nums:
            # Get an arbitrary value from the set
            current = next(iter(remaining_nums))

            # Step 1: Traverse backward to find the true start of the sequence
            while current - 1 in remaining_nums:
                current -= 1

            # Step 2: If there's no sequence upward either, remove and skip
            if current + 1 not in remaining_nums:
                remaining_nums.remove(current)
                continue

            # Step 3: Traverse forward and count the sequence length
            sequence_length = 0
            while current + sequence_length in remaining_nums:
                remaining_nums.remove(current + sequence_length)
                sequence_length += 1

            # Early exit if the sequence is large enough
            if sequence_length >= total_elements // 2:
                return sequence_length

            max_sequence_length = max(max_sequence_length, sequence_length)

        return max_sequence_length


# ✅ Test cases
solution = Solution()
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(solution.longestConsecutive([4, 0, -4, -2, 2, 5, 2, 0, -
      8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]))  # Output: 9


"""
🧠 Time Complexity: O(n)
- Each number is added to a set → O(n)
- Each number is removed from the set at most once
- No number is reprocessed, and lookups/removals are O(1)

📦 Space Complexity: O(n)
- The set stores all unique numbers from input

🚀 Why is this better than sorting?
- A sorting-based approach would take O(n log n) time.
- This avoids sorting altogether and uses hash-based set operations,
  achieving true linear time in the average and worst case.

✅ This is an efficient O(n) approach using a hash set and deletion to avoid reprocessing.
"""
