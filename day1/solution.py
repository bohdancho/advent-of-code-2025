lines = open("input.txt").read().split("\n")
lines.pop()
res = 0
cur = 50
for line in lines:
    direction = 1 if line[0] == "R" else -1
    num = int(line[1:])
    cur_before = cur
    cur += direction * num
    res += abs(cur) // 100
    if cur <= 0 and cur_before != 0:
        res += 1
    cur %= 100
print(res)
