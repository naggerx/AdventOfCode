import sys, re, time, itertools, functools, collections
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

ymax = len(lines)
xmax = len(lines[0])

seen = set()
res = 0
for y0,line in enumerate(lines):
    for x0,c0 in enumerate(line):
        if (x0,y0) in seen:
            continue
        area = 0
        fences = 0
        region = [(x0,y0)]
        while region:        
            x,y = region.pop()
            if (x,y) in seen:
                continue
            seen.add((x,y))
            area += 1
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                xx,yy = x+dx, y+dy
                if xx < 0 or xx >= xmax or yy < 0 or yy >= ymax:
                    fences += 1
                elif lines[yy][xx] != c0:
                    fences += 1
                else:
                    region.append((xx,yy))
        res += area * fences
        #print(f"{c0}  {area:2} * {fences:2} = {area*fences:4}   {res:5}")

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


seen = set()
res = 0
for y0,line in enumerate(lines):
    for x0,c0 in enumerate(line):
        if (x0,y0) in seen:
            continue

        area = 0
        fences = collections.defaultdict(set)
        
        region = [(x0,y0)]
        while region:        
            x,y = region.pop()
            #print("  ", x,y)
            if (x,y) in seen:
                continue
            seen.add((x,y))
            area += 1
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                xx,yy = x+dx, y+dy
                if xx < 0 or xx >= xmax or yy < 0 or yy >= ymax or lines[yy][xx] != c0:
                    fences[(dx, dy, y if dy else x)].add(x if dy else y)
                else:
                    region.append((xx,yy))
        f = len([x for xx in fences.values() for x in xx if x-1 not in xx])
        res += area * f
        #print(f"{c0}  {area:2} * {f:2} = {area*f:4}   {res:5}")

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
