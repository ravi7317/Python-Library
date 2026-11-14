# Moderate-level string exercises

text = input("Enter a string: ").strip()

# Remove extra spaces and display the normalized string
normalized = " ".join(text.split())
print("Normalized string:", normalized)

# Count vowels and words
vowels = "aeiouAEIOU"
vowel_count = sum(character in vowels for character in normalized)
word_count = len(normalized.split())
print("Vowel count:", vowel_count)
print("Word count:", word_count)

# Reverse words while preserving their order
reversed_words = " ".join(word[::-1] for word in normalized.split())
print("Words reversed:", reversed_words)

# Check whether the text is a palindrome (ignoring spaces and punctuation)
clean_text = "".join(character.lower() for character in normalized if character.isalnum())
print("Palindrome:", clean_text == clean_text[::-1])
