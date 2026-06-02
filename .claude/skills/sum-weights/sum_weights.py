#!/usr/bin/env python3
"""Read space-separated (left, right) pairs from stdin, print column sums."""

import sys

left_sum = 0.0
right_sum = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    try:
        l = float(parts[0])
        r = float(parts[1])
    except ValueError:
        continue
    left_sum += l
    right_sum += r
    count += 1

# If all values are integers, display as int
if left_sum == int(left_sum) and right_sum == int(right_sum):
    left_sum = int(left_sum)
    right_sum = int(right_sum)

total = left_sum + right_sum
if total == int(total):
    total = int(total)

print(f"左列总和: {left_sum}")
print(f"右列总和: {right_sum}")
print(f"总总和: {total}")
