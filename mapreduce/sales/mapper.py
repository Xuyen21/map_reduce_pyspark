#!/usr/bin/env python3
import sys
from itertools import combinations

current_order = None
products = []

for line in sys.stdin:
    # Remove leading/trailing whitespaces
    line = line.strip()
    if not line:
        continue

    # Split the fields
    fields = line.split(',')
    if len(fields) < 15:
        continue  # Skip invalid lines

    # Extract required fields
    order_id = fields[0]
    product_name = fields[4]
    department = fields[8]

    # Filter only products from "produce" department
    if department.lower() != "produce":
        continue

    # Process products by order
    if current_order == order_id:
        products.append(product_name)
    else:
        # Generate triplets for the previous order
        if current_order and len(products) >= 3:
            for triplet in combinations(sorted(products), 3):
                print(f'"{",".join(triplet)}"\t1')

        # Start a new order
        current_order = order_id
        products = [product_name]

# Process the last order
if current_order and len(products) >= 3:
    for triplet in combinations(sorted(products), 3):
        print(f'"{",".join(triplet)}"\t1')
