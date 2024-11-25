from collections import Counter

# Read the file and process the text
with open("sample.txt", "r") as file:
    text = file.read().lower()  # Convert text to lowercase

# Remove punctuation and split into words
words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).split()

# Count word frequencies
word_counts = Counter(words)

# Display the frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_counts.items():
    print(f"{word}: {freq}")

