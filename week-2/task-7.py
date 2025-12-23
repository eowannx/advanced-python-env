#Assignment 2 - task 7
from collections import Counter

items = input().split()
counter = Counter(items)
most_common = counter.most_common(1)[0][0]

purchased_once = []
for item in counter:
    if counter[item] == 1:
        purchased_once.append(item)

sorted_items = []
for item in counter:
    sorted_items.append((item, counter[item]))

print("Purchase frequency:")
for item in counter:
    print(f"{item}: {counter[item]}")

print(f"Most popular item: {most_common}")
print("Purchased once:", *purchased_once)

print("Sorted by frequency:")
for item, count in sorted_items:
    print(item, count)