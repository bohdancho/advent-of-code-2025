with open("input.txt") as file:
    tiles = [
        (int(a), int(b))
        for a, b in [row.split(",") for row in file.read().strip().split("\n")]
    ]
tiles_buf = [tiles[-1]] + tiles + [tiles[0]]

x_max, y_max = 0, 0

walls = set()
for i in range(1, len(tiles_buf) - 1):
    x_1, y_1 = tiles_buf[i]
    x_2, y_2 = tiles_buf[i + 1]

    x_max = max(x_max, x_1 + 1)
    y_max = max(y_max, y_1 + 1)

    if x_1 == x_2:
        for y in range(min(y_1, y_2) + 1, max(y_1, y_2)):
            walls.add((x_1, y))
    else:
        for x in range(min(x_1, x_2) + 1, max(x_1, x_2)):
            walls.add((x, y_1))


corners = dict()

for i in range(len(tiles)):
    corners[tiles[i]] = i

enclosed_cells = set()

# grid = [["." for _ in range(x_max)] for _ in range(y_max)]


def do_shit_with_corner(x, y):
    corner = tiles[corners[(x, y)]]
    prev_corner = tiles[corners[(x, y)] - 1]
    prev_prev_corner = tiles[corners[(x, y)] - 2]

    if corners[(x, y)] + 1 == len(tiles):
        next_corner = tiles[0]
        next_next_corner = tiles[1]
    elif corners[(x, y)] + 2 == len(tiles):
        next_corner = tiles[-1]
        next_next_corner = tiles[0]
    else:
        next_corner = tiles[corners[(x, y)] + 1]
        next_next_corner = tiles[corners[(x, y)] + 2]

    print(x, y, prev_prev_corner, prev_corner, corner, next_corner, next_next_corner)

    if prev_corner[0] > corner[0]:
        return (
            (prev_corner[1] - prev_prev_corner[1]) * (next_corner[1] - corner[1])
        ) > 0, prev_corner[0] + 1
    else:
        return (
            (next_corner[1] - corner[1]) * (prev_corner[1] - prev_prev_corner[1])
        ) > 0, next_corner[0] + 1


for y in range(y_max):
    print(y / y_max)
    is_enclosed = False
    x = 0
    while x < x_max:
        if (x, y) in corners:
            flip, next_x = do_shit_with_corner(x, y)
            print(x, y, flip, next_x)
            if flip:
                is_enclosed = not is_enclosed
            x = next_x
            continue

        if (x, y) in walls:
            is_enclosed = not is_enclosed
            x += 1
            continue

        if is_enclosed:
            enclosed_cells.add((x, y))
        x += 1

# for x, y in corners:
#     grid[y][x] = "#"
#
# for x, y in walls:
#     grid[y][x] = "X"
#
# for x, y in enclosed_cells:
#     grid[y][x] = "O"

# print("\n".join("".join(row) for row in grid))
