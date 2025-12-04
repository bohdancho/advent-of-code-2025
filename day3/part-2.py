data = open("input.txt").read().strip().split("\n")

res = 0
for line in data:
    i = 0
    for j in range(12):
        for k in range(i, len(line) - (12 - j) + 1):
            if int(line[k]) > int(line[i]):
                i = k
        res += 10 ** (11 - j) * int(line[i])
        i += 1

print(res)
