"""Generate random Python and data-structures practice questions."""

import random


QUESTIONS = {
	"strings": [
		"Check whether a string is a palindrome.",
		"Count the vowels in a string, ignoring case.",
		"Find the first non-repeating character in a string.",
	],
	"lists": [
		"Find the second-largest distinct number in a list.",
		"Remove duplicates from a list while preserving order.",
		"Rotate a list to the right by k positions.",
	],
	"algorithms": [
		"Implement binary search on a sorted list.",
		"Sort a list using insertion sort.",
		"Merge two sorted lists into one sorted list.",
	],
	"dictionaries and sets": [
		"Count how often each word occurs in a sentence.",
		"Find the values shared by two lists.",
		"Check whether two strings are anagrams, ignoring case and spaces.",
	],
}


def generate_questions(topic="all", count=3):
	"""Return up to count unique questions for the selected topic."""
	topic = topic.lower().strip()
	if topic == "all":
		available = [question for group in QUESTIONS.values() for question in group]
	elif topic in QUESTIONS:
		available = QUESTIONS[topic][:]
	else:
		raise ValueError(f"Choose 'all' or one of: {', '.join(QUESTIONS)}")

	if count < 1:
		raise ValueError("Count must be at least 1.")
	return random.sample(available, min(count, len(available)))


def main():
	print("Python & DSA Practice Generator")
	print("Topics:", ", ".join(QUESTIONS))
	topic = input("Choose a topic or type 'all' [all]: ").strip() or "all"

	try:
		count = int(input("Number of questions [3]: ").strip() or "3")
		questions = generate_questions(topic, count)
	except ValueError as error:
		print("Invalid input:", error)
		return

	print("\nPractice questions:")
	for number, question in enumerate(questions, start=1):
		print(f"{number}. {question}")


if __name__ == "__main__":
	main()
