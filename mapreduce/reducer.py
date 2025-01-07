#!/usr/bin/python3

import sys
from collections import defaultdict

def reducer():
    count_dict = defaultdict(int)

    for line in sys.stdin:
        try:
            # Parse input line by removing unwanted characters
            key, value = line.strip().split('\t')
            key = key.replace("(", "").replace(")", "").replace("'", "").replace(" ", "")
            count_dict[key] += int(value)
        except Exception as e:
            continue

    for key, count in count_dict.items():
        print(f"{key}\t{count}")

if __name__ == "__main__":
    reducer()
