def binary_search(arr, target):
    """Return the index of target in a sorted list, or -1 if absent."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [2, 4, 7, 10, 18, 23]
    print(binary_search(numbers, 10))
