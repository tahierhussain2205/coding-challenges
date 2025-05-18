# Trapping Rain Water

## Problem

You are given an array of non-negative integers `height` where each element represents the height of a bar in an elevation map. The width of each bar is 1.

Your task is to compute how much water it can trap **after raining**.

---

## Example 1:

**Input:**  
`height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]`  
**Output:**  
`9`

**Explanation:**  
The image below shows how water is trapped (blue) between the bars (black):

![Trapped Rain Water](rainwatertrap.png "Visualization of Trapped Rain Water")

---

## Constraints:

- `1 <= height.length <= 1000`
- `0 <= height[i] <= 1000`

---

## Recommended Time & Space Complexity:

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) or better
