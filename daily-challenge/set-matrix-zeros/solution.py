class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None. Do not return anything, modify matrix in-place instead.
        """

        # Sets to track rows and columns that contain at least one zero
        zero_rows = set()
        zero_cols = set()

        # First pass: identify all rows and columns that need to be zeroed
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Second pass: update the matrix in-place
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0

        return matrix


# ✅ Test cases
solution = Solution()
print(solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

print(solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


"""
🕒 Time Complexity: O(m × n)
We loop through the entire matrix twice:
  - Once to identify rows and columns with zeroes
  - Once to set values to zero based on marked rows and columns
So total time = O(m × n), where m = number of rows, n = number of columns

🧠 Space Complexity: O(m + n)
We use extra space for two sets:
  - One for storing up to m row indices
  - One for storing up to n column indices
Hence, space = O(m + n)
"""
