#!/usr/bin/env python3
import sys
from collections import defaultdict

char_count = defaultdict(int)

# Process input lines
for line in sys.stdin:
    line = line.strip()
    char, count = line.split('\t')
    char_count[char] += int(count)

# Output the character counts
for char, count in char_count.items():
    print(f"{char}\t{count}")

