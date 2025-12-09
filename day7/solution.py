# # 7:53
#
# data = open("input.txt").read().strip().split("\n")
# y_max = len(data)
# x_max = len(data[0])
# x_start, y_start = data[0].find("S"), 0
#
#
# def req(x, y, visited):
#     if not (0 <= x < x_max) or not (0 <= y < y_max) or (x, y) in visited:
#         return 0
#
#     visited.add((x, y))
#     if data[y][x] == ".":
#         return req(x, y + 1, visited)
#     else:
#         return 1 + req(x - 1, y, visited) + req(x + 1, y, visited)
#
#
# print(req(x_start, y_start, set()))

from functools import cache

data = open("input.txt").read().strip().split("\n")
y_max = len(data)
x_max = len(data[0])
x_start, y_start = data[0].find("S"), 0


@cache
def req(x, y):
    if not (0 <= x < x_max) or not (0 <= y < y_max):
        return 1

    if data[y][x] == ".":
        return req(x, y + 1)
    else:
        return req(x - 1, y) + req(x + 1, y)


print(req(x_start, y_start))
