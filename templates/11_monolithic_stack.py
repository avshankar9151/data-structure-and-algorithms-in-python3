"""
🧱 What is a Monotonic Stack?

A monotonic stack is a stack (LIFO data structure) that maintains its elements in either increasing or decreasing order.

Monotonic Increasing Stack: Elements increase from top to bottom
👉 Good for finding next smaller elements

Monotonic Decreasing Stack: Elements decrease from top to bottom
👉 Good for finding next greater elements
---------------------------------------------------
✅ Why use it?

To efficiently solve problems like:

Next Greater Element

Largest Rectangle in Histogram

Trapping Rain Water

Sliding Window Maximum

Daily Temperatures

Instead of O(n²) brute force, you get O(n) time!
---------------------------------------------------
💡 Key Idea

You iterate through the array and maintain a stack such that it preserves a monotonic order.
As you go, you pop from the stack until the order is restored — this is how you discard elements you don't need.
"""

def nextGreaterElements(nums):
    result = [-1] * len(nums)
    stack = []  # stores indices

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
