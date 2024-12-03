import sys

with open("02_in.txt") as f:
    lines = f.readlines()


res = 0
for line in lines:
    e = list(map(int,line.split(' ')))

    diffs = list(a-b for a,b in zip(e[1:],e[:-1]))

    if max(diffs) <= 3 and min(diffs) >= 1:
        res += 1
    if max(diffs) <= -1 and min(diffs) >= -3:
        res += 1

print("Part1:", res)

res = 0
for line in lines:
    e = list(map(int,line.split(' ')))

    for i in range(len(e)):
        e2 = e[:i] + e[i+1:]

        diffs = list(a-b for a,b in zip(e2[1:],e2[:-1]))

        if max(diffs) <= 3 and min(diffs) >= 1:
            res += 1
            break
        if max(diffs) <= -1 and min(diffs) >= -3:
            res += 1
            break

print("Part2:", res)
