def binary_search(values, target):
	"""Return the index of target in a sorted list, or -1 if it is absent."""
	left, right = 0, len(values) - 1

	while left <= right:
		middle = (left + right) // 2
		if values[middle] == target:
			return middle
		if values[middle] < target:
			left = middle + 1
		else:
			right = middle - 1

	return -1


if __name__ == "__main__":
	numbers = [2, 5, 8, 12, 16, 23, 38]
	target = 16
	result = binary_search(numbers, target)
	print(f"{target} found at index {result}" if result != -1 else "Not found")
