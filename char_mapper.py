#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    for char in line:
        if char != ' ':  # Ignore spaces if not needed
            print(f"{char}\t1")

