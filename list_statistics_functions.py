"""
functions.py
A simple utility module for basic list operations:
sum, max, min, average, range, and normalization.
"""

def sum_lst(nums):
    total = 0
    for i in nums:
        total += i
    return total


def max_lst(nums):
    mx = nums[0]
    for num in nums:
        if num > mx:
            mx = num
    return mx


def min_lst(nums):
    mn = nums[0]
    for num in nums:
        if num < mn:
            mn = num
    return mn


def average_lst(nums):
    sm = sum(nums)
    cnt = len(nums)
    return sm / cnt


def rng(nums):
    return max_lst(nums) - min_lst(nums)


def normalize(nums):
    min_val = min_lst(nums)
    max_val = max_lst(nums)

    if max_val == min_val:
        return [0 for _ in nums]  # avoids division by zero

    normalized = []
    for x in nums:
        n = (x - min_val) / (max_val - min_val)
        normalized.append(n)

    return normalized


# Example 

if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]
    print("Sum:", sum_lst(lst1))

    lst2 = [1, 2, 3, 5, 4]
    print("Max:", max_lst(lst2))

    lst3 = [12, 2332, 322, 3222992, 393993]
    print("Min:", min_lst(lst3))

    lst4 = [1, 2, 3, 4, 5, 6, 76]
    print("Average:", average_lst(lst4))

    lst5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Range:", rng(lst5))

    lst6 = [10, 20, 30, 40, 50]
    print("Normalized:", normalize(lst6))