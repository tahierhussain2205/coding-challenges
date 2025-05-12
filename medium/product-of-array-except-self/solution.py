from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Count of zeros and the total product of all non-zero elements
        zero_count = 0
        total_product = 1
        result = [0] * len(nums)  # Initialize output list with zeros

        # First pass: calculate total product and count zeros
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    # If more than one zero, all products will be zero
                    return result
                continue
            total_product *= num

        # Second pass: build result list based on zero count
        for index, num in enumerate(nums):
            if zero_count:
                if num == 0:
                    # Only the position of the zero gets the product
                    result[index] = total_product
                    return result  # Early exit
                # All other positions stay 0 (already set)
            else:
                # No zeros: divide total product by current number
                result[index] = total_product // num

        return result


# ✅ Test Cases
solution = Solution()

# Case 1: No zeros, basic case
print(solution.productExceptSelf([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]

# Case 2: Two zeros, output should be all zeros
print(solution.productExceptSelf([0, 0]))
# Output: [0, 0]

# Case 3: One zero, only one non-zero position
print(solution.productExceptSelf([0, 1, 2, 3]))
# Output: [6, 0, 0, 0]

# Case 4: Negative numbers
print(solution.productExceptSelf([-1, 2, -3, 4]))
# Output: [-24, 12, -8, 6]

# Case 5: All same elements
print(solution.productExceptSelf([2, 2, 2, 2]))
# Output: [8, 8, 8, 8]


"""
🕒 Time Complexity:
- O(n) for the first pass (counting and product)
- O(n) for the second pass (building result)
=> Total: O(n)

🧠 Space Complexity:
- O(n) for the output list
- O(1) extra space (for variables like total_product, zero_count, etc.)
=> Total: O(n)
"""
