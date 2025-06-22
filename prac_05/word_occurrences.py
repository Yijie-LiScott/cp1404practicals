"""
Word Occurrences
Estimate: 18 minutes
Actual:   14 minutes
"""

text = input("Text: ")
words = text.split()
word_counts = {}

for word in words:
    word = word.lower()  # Normalize to lowercase
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort words alphabetically
sorted_words = sorted(word_counts.keys())

# Find the length of the longest word for formatting
max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}} : {word_counts[word]}")