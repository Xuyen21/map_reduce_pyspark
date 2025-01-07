#!/usr/bin/env python3
import sys
from collections import defaultdict

triplet_counts = defaultdict(int)

# Read input from mapper
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Parse input
    triplet, count = line.rsplit('\t', 1)
    count = int(count)
    triplet_counts[triplet] += count

# Sort by count in descending order and keep the top 3
sorted_triplets = sorted(triplet_counts.items(), key=lambda x: x[1], reverse=True)

# Output the top 3 triplets
for triplet, count in sorted_triplets[:3]:
    print(f'{triplet}\t{count}')

