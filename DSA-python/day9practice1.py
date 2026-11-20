"""Day 9 DSA practice: searching and common array problems."""


def linear_search(numbers, target):
	for index, value in enumerate(numbers):
		if value == target:
			return index
	return -1


def binary_search(sorted_numbers, target):
	"""Return the target index in a sorted list, or -1 if absent."""
	low, high = 0, len(sorted_numbers) - 1
	while low <= high:
		middle = (low + high) // 2
		if sorted_numbers[middle] == target:
			return middle
		if sorted_numbers[middle] < target:
			low = middle + 1
		else:
			high = middle - 1
	return -1


def two_sum(numbers, target):
	"""Return indices of two numbers whose sum equals target, if found."""
	seen = {}
	for index, value in enumerate(numbers):
		complement = target - value
		if complement in seen:
			return seen[complement], index
		seen[value] = index
	return None


def is_palindrome(text):
	cleaned = "".join(char.lower() for char in text if char.isalnum())
	return cleaned == cleaned[::-1]


if __name__ == "__main__":
	data = [3, 7, 11, 18, 24, 31]
	print("Linear search:", linear_search(data, 18))
	print("Binary search:", binary_search(data, 24))
	print("Two sum:", two_sum([2, 8, 5, 1], 9))
	print("Palindrome:", is_palindrome("Never odd or even"))
