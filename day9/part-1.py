with open("input.txt") as file:
    tiles = [
        (int(a), int(b))
        for a, b in [row.split(",") for row in file.read().strip().split("\n")]
    ]

res = 0
for i in range(len(tiles)):
    a = tiles[i]
    for j in range(i + 1, len(tiles)):
        b = tiles[j]
        res = max(res, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))

print(res)
