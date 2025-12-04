data = open("input.txt").readline().strip()

res = 0
for interval in data.split(","):
    lo, hi = interval.split("-")
    for n in range(int(lo), int(hi) + 1):
        s = str(n)
        for l in range(1, len(s) // 2 + 1):
            if len(s) % l != 0:
                continue

            valid = True
            for i in range(0, len(s) - l + 1, l):
                if s[i : i + l] != s[:l]:
                    valid = False
                    break

            if valid:
                res += n
                break
print(res)
