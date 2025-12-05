# 0 3 5 10 14 15 20 12 18

# 0 3 5 10 14 16 20 inf
# 0 3 5 10 20 inf
import math
import bisect

ranges_raw, values = open("input.txt").read().strip().split("\n\n")

ranges = [0, math.inf]
for r in ranges_raw.split("\n"):
    lo, hi = r.split("-")
    lo, hi = int(lo), int(hi)

    lo_index = bisect.bisect_left(ranges, lo)
    hi_index = bisect.bisect_left(ranges, hi)

    ranges = ranges[:lo_index] + ranges[hi_index:]

    if hi_index % 2 == 1:
        ranges.insert(lo_index, hi)
    if lo_index % 2 == 1:
        ranges.insert(lo_index, lo)

# part 1
# res = 0
# for line in values.split("\n"):
#     value = int(line)
#     idx = bisect.bisect_left(ranges, value)
#     if idx % 2 == 0 or ranges[idx] == value:
#         res += 1

# part 2
print(ranges)
res = 0
corrections = set()
for i in range(1, len(ranges) - 2, 2):
    res += max(ranges[i + 1] - ranges[i] - 1, 0)
    if ranges[i] not in corrections:
        res += 1
        corrections.add(ranges[i])

    if ranges[i + 1] not in corrections:
        res += 1
        corrections.add(ranges[i + 1])

# 0 3 3 3 4 inf
# print(len(ranges), len(set(ranges)))

print(res)
