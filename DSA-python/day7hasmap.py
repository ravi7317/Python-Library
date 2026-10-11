# HashMap (Dictionary) Question: Two Sum
# Given a list of integers and a target, return the indices of two numbers
# whose sum equals the target.


def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []


# Example
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  # [0, 1]
