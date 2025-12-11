from functools import cache


with open("input.txt") as file:
    data = file.read().strip().split("\n")

adj = {}
starts = []
for line in data:
    source, dests = line.split(": ")
    adj[source] = dests.split(" ")


@cache
def req(node, has_dac, has_fft):
    if node == "out":
        return 1 if has_dac and has_fft else 0
    res = 0
    res += sum(
        req(node1, has_dac or node == "dac", has_fft or node == "fft")
        for node1 in adj[node]
    )
    return res


print(req("svr", False, False))
