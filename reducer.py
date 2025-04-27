import sys
from collections import defaultdict
# Initialize a dictionary to hold word counts
word_count = defaultdict(int)
# Read input from standard input (stdin)
for line in sys.stdin:
	line = line.strip() # Remove leading/trailing whitespace
	word, count = line.split('\t') # Split the input by tab

	word_count[word] += int(count) # Add the count to the word's total
# Output the word counts
for word, count in word_count.items():
	print(f"{word}\t{count}")
