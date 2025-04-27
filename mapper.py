import sys
# Read input from standard input (stdin)
for line in sys.stdin:
	line = line.strip() # Remove leading/trailing whitespace
	words = line.split() # Split the line into words
	for word in words:
		print(f"{word}\t1") # Output the word with a count of 1
