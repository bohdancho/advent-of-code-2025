from shapely.geometry import Point, Polygon


with open("input.txt") as file:
    corners = [
        (int(a), int(b))
        for a, b in [row.split(",") for row in file.read().strip().split("\n")]
    ]

p = Polygon(corners)
print(Point(7, 1).within(p))

# res = 0
# for i in range(len(corners)):
#     a = corners[i]
#     for j in range(i + 1, len(corners)):
#         b = corners[j]
#         res = max(res, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
#
# print(res)
