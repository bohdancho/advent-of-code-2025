from collections import defaultdict
from math import prod

data = open("input.txt").read().strip().split("\n")
cols = defaultdict(list)
for row in data:
    row += " "
    i = 0
    pointer = 0
    while True:
        numstart = pointer + len(row[pointer:]) - len(row[pointer:].lstrip())
        if numstart == len(row):
            break
        numend = numstart + row[numstart:].find(" ")
        cols[i].append((row[numstart:numend], numstart))
        i += 1
        pointer = numend


res = 0
for col in cols.values():
    operator = col.pop()
    nums = []

    min_idx = min([idx for _, idx in col])
    max_idx = max([idx + len(n) - 1 for n, idx in col])

    for idx in range(max_idx, min_idx - 1, -1):
        cur = ""
        for row in data[:-1]:
            if row[idx] != " ":
                cur += row[idx]
        nums.append(int(cur))

    if operator[0] == "+":
        res += sum(nums)
    else:
        res += prod(nums)

print(res)
