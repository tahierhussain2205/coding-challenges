from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Map to track positions of each digit seen so far
        digit_positions = {}

        # Loop through every cell in the board
        for row in range(len(board)):
            for col in range(len(board[row])):
                cell_value = board[row][col]

                # Skip empty cells
                if cell_value == '.':
                    continue

                # If digit is seen for the first time, initialize with its position
                if cell_value not in digit_positions:
                    digit_positions[cell_value] = [(row, col)]
                    continue

                # Check all previously seen positions of the same digit
                for prev_row, prev_col in digit_positions[cell_value]:
                    # Rule 1: Same row conflict
                    if prev_row == row:
                        return False

                    # Rule 2: Same column conflict
                    if prev_col == col:
                        return False

                    # Rule 3: Same 3x3 sub-box conflict
                    if prev_row // 3 == row // 3 and prev_col // 3 == col // 3:
                        return False

                # If no conflict, add the new position
                digit_positions[cell_value].append((row, col))

        # If no conflicts found, the board is valid
        return True


# ✅ Test cases
solution = Solution()

# Valid board
print(solution.isValidSudoku([
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))  # Output: True

# Invalid board (duplicate '1' in top-left sub-box)
print(solution.isValidSudoku([
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))  # Output: False

"""
🧠 Time Complexity: O(n² * m)
- n = 9 (rows/columns)
- m = number of previous positions per digit (max 8)
- Worst case: O(81 × 8) = O(648)

📦 Space Complexity: O(n²)
- Stores positions of digits as (row, col) tuples in a dictionary
- Up to 81 total positions if board is full
"""
