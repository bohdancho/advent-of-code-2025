import math
from heapq import *
from collections import Counter

with open("input.txt") as file:
    data = [[int(n) for n in row.split(",")] for row in file.read().strip().split("\n")]

distances = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        d = math.sqrt(
            (data[i][0] - data[j][0]) ** 2
            + (data[i][1] - data[j][1]) ** 2
            + (data[i][2] - data[j][2]) ** 2
        )
        distances.append((d, i, j))

heapify(distances)


parents = list(range(len(data)))


def get_root(i):
    if parents[i] == i:
        return i
    return get_root(parents[i])


prev = None
while True:
    _, i, j = heappop(distances)
    root_i, root_j = get_root(i), get_root(j)
    parents[root_i] = root_j

    roots = set(get_root(idx) for idx in range(len(parents)))
    if len(roots) == 1:
        break

    prev = (i, j)

print(data[i][0] * data[j][0])
