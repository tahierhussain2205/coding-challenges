from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search range: minimum possible sum to maximum possible sum
        min_possible_sum = max(nums)  # At least one element per subarray
        max_possible_sum = sum(nums)  # All elements in one subarray
        nums_length = len(nums)

        optimal_sum = max_possible_sum

        while min_possible_sum <= max_possible_sum:
            mid = (min_possible_sum + max_possible_sum) // 2

            # Check if we can split array into k subarrays with max sum <= mid
            required_subarrays = 1
            current_subarray_sum = 0

            for element in nums:
                # If single element exceeds candidate sum, impossible split
                if element > mid:
                    required_subarrays = k + 1
                    break

                # If adding current element exceeds limit, start new subarray
                if current_subarray_sum + element > mid:
                    current_subarray_sum = element
                    required_subarrays += 1
                else:
                    current_subarray_sum += element

                # Early termination if too many subarrays needed
                if required_subarrays > k:
                    break

            # Adjust binary search bounds based on feasibility
            if required_subarrays > k:
                min_possible_sum = mid + 1
            else:
                max_possible_sum = mid - 1

            # Update result if valid split found
            if required_subarrays == k or (required_subarrays < k and nums_length - required_subarrays >= k - required_subarrays):
                optimal_sum = min(optimal_sum, mid)

        return optimal_sum


# Test cases
solution = Solution()
print(solution.splitArray([2, 4, 10, 1, 5], 2))  # Expected: 16
print(solution.splitArray([1, 0, 2, 3, 5], 4))   # Expected: 5

# Time Complexity: O(n * log(sum - max))
# - Binary search runs in O(log(sum - max)) iterations
# - Each iteration requires O(n) to validate the split
#
# Space Complexity: O(1)
# - Only using constant extra space for variables
#
# Algorithm: Binary search on the answer
# - Search space is between max(nums) and sum(nums)
# - For each candidate sum, check if array can be split into k subarrays
# - Use greedy approach: pack elements until sum would exceed limit
