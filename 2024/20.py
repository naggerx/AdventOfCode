import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

ymax = len(lines)
xmax = len(lines[0])


sx,sy = 0,0
ex,ey = xmax-1,ymax-1

grid = set()
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == '#':
            grid.add((x,y))
        if c == 'S':
            sx,sy = x,y
        if c == 'E':
            ex,ey = x,y


adj4 = ((0,-1), (0,1), (-1,0), (1,0))
seen = {(sx,sy):0}
q = [(0, sx,sy)]
while len(q):
    c,x,y = heapq.heappop(q)
    if (x,y) == (ex,ey):
        break
    for dx,dy in adj4:
        nc, nx, ny = c+1, x+dx, y+dy
        if (nx,ny) not in grid and 0 <= nx < xmax and 0 <= ny < ymax:
            if nc < seen.get((nx,ny), 100000):
                seen[nx,ny] = nc
                heapq.heappush(q, (nc,nx,ny))
else:
    raise "no path found"

#print('\n'.join([''.join([('###' if (x,y) in grid else (f"{seen[x,y]%100:^3}" if (x,y) in seen else '   ')) for x in range(xmax)]) for y in range(ymax)]))

res = 0
cnt = dd(int)
for y in range(1,ymax-1):
    for x in range(1,xmax-1):
        c = seen.get((x,y))
        if c is not None:
            for dx,dy in adj4:
                nx,ny = x+dx,y+dy
                nx2,ny2 = x+dx+dx,y+dy+dy
                c2 = seen.get((nx2,ny2))
                if (nx,ny) in grid and c2 is not None:
                    diff = c2 - c - 2
                    if diff > 0:
                        cnt[diff] += 1
                        if diff >= 100:
                            res += 1

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

clen = 20

res = 0
cnt = dd(int)
for (x1,y1),c1 in seen.items():
    for dx in range(-clen,clen+1):
        for dy in range(-clen,clen+1):
            if abs(dx) + abs(dy) <= clen:
                if (c2 := seen.get((x1 + dx, y1 + dy))) is not None:
                    diff = c2 - c1 - abs(dx) - abs(dy)
                    if diff > 0:
                        cnt[diff] += 1
                        if diff >= 100:
                            res += 1
for i in sorted(cnt)[-15:]:
    print(cnt[i],i)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

res = 0
cnt = dd(int)
for y in range(1,ymax-1):
    for x in range(1,xmax-1):
        if (c1 := seen.get((x,y))) is not None:
            for dx in range(-clen,clen+1):
                for dy in range(-clen,clen+1):
                    if abs(dx) + abs(dy) <= clen:
                        if (c2 := seen.get((x+dx,y+dy))) is not None:
                            diff = c2 - c1 - abs(dx) - abs(dy)
                            if diff > 0:
                                cnt[diff] += 1
                                if diff >= 100:
                                    res += 1
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


res = 0
for (x1,y1),c1 in seen.items():
    for (x2,y2),c2 in seen.items():
        if abs(x1-x2) + abs(y1-y2) <= clen:
            if c2 - c1 - abs(x1-x2) - abs(y1-y2) >= 100:
                res += 1
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
