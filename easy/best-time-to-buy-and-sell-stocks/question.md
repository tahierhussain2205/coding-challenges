# Best Time to Buy and Sell Stock

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `i`th day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the **maximum profit** you can achieve. You may choose to not make any transactions, in which case the profit would be `0`.

---

## Example 1

**Input:**  
`prices = [10,1,5,6,7,1]`

**Output:**  
`6`

**Explanation:**  
Buy on day 1 (price = 1) and sell on day 4 (price = 7). Profit = 7 - 1 = 6.

---

## Example 2

**Input:**  
`prices = [10,8,7,5,2]`

**Output:**  
`0`

**Explanation:**  
No profitable transactions can be made.

---

## Constraints

- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`
