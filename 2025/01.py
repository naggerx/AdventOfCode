import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

pos = 50
res = 0
for line in lines:
    dir = -1 if line[0] == 'L' else 1
    steps = int(line[1:])
    pos = (pos + dir * steps) % 100
    if pos == 0:
        res += 1
    #print(line, dir, steps, pos, res)


print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

pos = 50
res = 0
for line in lines:
    dir = -1 if line[0] == 'L' else 1   
    for i in range(int(line[1:])):
        pos = (pos + dir) % 100
        if pos == 0:
            res += 1

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
