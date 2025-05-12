from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # Step 2: Create buckets. Each index represents frequency,
        # and the value at each index is a list of numbers with that frequency.
        max_freq = len(nums)
        buckets = [[] for _ in range(max_freq + 1)]

        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        # Step 3: Traverse buckets in reverse (from high freq to low),
        # and collect the top k frequent elements
        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result  # In case input is invalid (but problem guarantees valid input)


# Test cases
solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2))  # Output: [3, 1]
print(solution.topKFrequent([1], 1))                             # Output: [1]


"""
🕒 Time Complexity:
- Counting frequencies: O(n)
- Bucketing values: O(n)
- Collecting top k elements: O(n) in worst case
→ Overall: O(n), where n is the length of the input list

🧠 Space Complexity:
- Frequency map: O(n)
- Buckets: O(n)
- Result list: O(k)
→ Overall: O(n)

🚀 Why Bucket Sort is Efficient Here:

- A naive approach would sort elements based on frequency → O(n log n)
- But bucket sort leverages the fact that:
  - The maximum frequency of any number is at most `n`
  - So we can create an array of `n+1` buckets where index = frequency
- By inserting numbers into these buckets and iterating from high to low,
  we avoid sorting altogether, achieving **linear time performance (O(n))**

This makes the bucket sort method optimal for this problem compared to a sorting-based approach.
"""
