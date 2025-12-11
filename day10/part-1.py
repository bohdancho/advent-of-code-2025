import math

with open("input.txt") as file:
    data = file.read().strip().split("\n")

res = 0

for line in data:
    target_str, remainder = line.split("] ")
    target_str = target_str.lstrip("[")

    target = 0
    for i, c in enumerate(target_str):
        if c == "#":
            target += 1 << i

    permutations = []
    for perm_str in remainder[: remainder.find(" {")].split(" "):
        digits = perm_str.removeprefix("(").removesuffix(")").split(",")
        perm = 0
        for digit in digits:
            perm += 1 << int(digit)
        permutations.append(perm)

    dp = {0: 0}
    while target not in dp:
        prev, dp = dp, {}
        for perm in permutations:
            for k, v in prev.items():
                dp[k ^ perm] = min(v + 1, dp.get(k ^ perm, math.inf))
    res += dp[target]

print(res)
