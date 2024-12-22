import sys, re, time, itertools, functools, heapq, collections, bisect
from collections import defaultdict as dd
from heapq import heappush, heappop
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

if len(lines) > 50:
    xmax = 71
    num_part1 = 1024
else:
    xmax = 7
    num_part1 = 12
ymax = xmax


adj4 = ((0,1), (1,0), (0,-1), (-1,0))
sx,sy = 0,0
ex,ey = xmax-1,ymax-1


def find_route(num_bytes):
    grid = set()
    for ln, line in enumerate(lines[:num_bytes]):
        gx,gy = map(int,re.findall(r'-?\d+', line))
        grid.add((gx,gy))

    seen = {(sx,sy):0}
    q = [(0, sx,sy)]
    while len(q):
        c,x,y = heappop(q)
        if (x,y) == (ex,ey):
            print(" find_route", num_bytes, "->", c)
            return c
        for dx,dy in adj4:
            nc, nx, ny = c+1, x+dx, y+dy
            if (nx,ny) not in grid and 0 <= nx < xmax and 0 <= ny < ymax:
                if nc < seen.get((nx,ny), 100000):
                    seen[nx,ny] = nc                
                    heappush(q, (nc,nx,ny))
    print(" find_route", num_bytes, "->", None)
    return None


res = find_route(num_part1)
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

i = bisect.bisect_left(range(len(lines)), True, key=lambda x: find_route(x) is None)
res = lines[i - 1]
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")

i = bisect.bisect_right(range(len(lines)), False, key=lambda x: find_route(x) is None)
res = lines[i - 1]
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")

#starttime = time.time()
