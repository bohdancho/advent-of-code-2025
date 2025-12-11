import math

with open("input.txt") as file:
    data = file.read().strip().split("\n")

res = 0

for i, line in enumerate(data):
    print(i / len(data))
    remainder, target_str = line.split(" {")
    target = tuple(int(n) for n in target_str.removesuffix("}").split(","))

    increases = []
    for increase_str in remainder[remainder.find("] ") + 2 :].split(" "):
        increases.append(
            list(
                int(n)
                for n in increase_str.removeprefix("(").removesuffix(")").split(",")
            )
        )

    dp = {tuple(0 for _ in range(len(target))): 0}
    idx = 0
    while target not in dp and idx < 2:
        prev, dp = dp, {}
        for increase in increases:
            for k, v in prev.items():
                increased = list(k)
                for n in increase:
                    increased[n] += 1
                increased = tuple(increased)
                for i in range(len(increased)):
                    if increased[i] > target[i]:
                        continue
                dp[increased] = min(v + 1, dp.get(increased, math.inf))
        print(len(dp))
    res += dp[target]

print(res)
