import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

ymax = len(lines)
xmax = len(lines[0])

adj8 = ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1))

res = 0
for y in range(ymax):
    for x in range(xmax):
        if lines[y][x] == '@':
            blocked = 0
            for dx,dy in adj8:
                nx,ny = x+dx, y+dy
                if 0 <= nx < xmax and 0 <= ny < ymax and lines[ny][nx] == '@':
                    blocked += 1
            if blocked < 4:
                res += 1

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


lines = list(map(list, lines))
res = 0

rem = -1
while rem != 0:
    rem = 0
    for y in range(ymax):
        for x in range(xmax):
            if lines[y][x] == '@':
                blocked = 0
                for dx,dy in adj8:
                    nx,ny = x+dx, y+dy
                    if 0 <= nx < xmax and 0 <= ny < ymax and lines[ny][nx] == '@':
                        blocked += 1
                if blocked < 4:
                    lines[y][x] = '.'
                    rem += 1
    res += rem

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
