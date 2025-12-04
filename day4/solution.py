grid = [list(row) for row in open("input.txt").read().strip().split("\n")]
y_max = len(grid)
x_max = len(grid[0])

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
res = 0

while True:
    cur = 0

    for y in range(y_max):
        for x in range(x_max):
            if grid[y][x] != "@":
                continue

            adj = 0
            for x_delta, y_delta in deltas:
                if (0 <= x + x_delta < x_max) and (0 <= y + y_delta < y_max):
                    if grid[y + y_delta][x + x_delta] == "@":
                        adj += 1

            if adj < 4:
                cur += 1
                grid[y][x] = "."

    if cur > 0:
        res += cur
    else:
        break

print(res)
