data = open("input.txt").read().strip().split("\n")

res = 0
for line in data:
    largestIdx = 0
    for i in range(len(line) - 1):
        if int(line[i]) > int(line[largestIdx]):
            largestIdx = i

    secondLargest = largestIdx + 1
    for i in range(largestIdx + 1, len(line)):
        if int(line[i]) > int(line[secondLargest]):
            secondLargest = i

    res += int(line[largestIdx]) * 10 + int(line[secondLargest])

print(res)
