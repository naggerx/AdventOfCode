import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

res = 0
rays = [0] * len(lines[0])
for line in lines:
    for i, ch in enumerate(line):
        if ch == 'S':
            rays[i] = 1
        elif ch == '^':
            if rays[i] > 0:
                res += 1
            rays[i-1] += rays[i]
            rays[i+1] += rays[i]
            rays[i] = 0
    #print(''.join(['|' if c == '.' and r > 0 else c for c,r in zip(line, rays)]), rays)

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
print(f"Part2: {sum(rays)}  ({time.time()-starttime:.3}s)")
