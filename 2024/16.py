import sys, re, time, itertools, functools, bisect
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

ymax = len(lines)
xmax = len(lines[0])

grid = set()
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c in 'SE.':
            grid.add((x,y))
            if c == 'S':
                rx,ry = x,y
            elif c == 'E':
                fx,fy = x,y


seen = {}

q = [(0, (rx,ry,1,0), 0, None)]

res = 100000000000
nodes = set()
while len(q):
    restcost,pose,cost,prev = q.pop(0)
    x,y,dx,dy = pose
    
    #print(i, restcost, cost, pose, len(q))
    if restcost > res:
        break

    s = seen.get(pose)
    if s:
        if cost == s[0]:
            seen[pose] = (cost, s[1] | {prev})
        continue
    seen[pose] = (cost, {prev})

    if x == fx and y == fy:
        nodes.add(pose)
        nodes.add(prev)
        res = cost

    for nx,ny,ndx,ndy,nc in ((x,y,dy,-dx,cost+1000), (x,y,-dy,dx,cost+1000), (x+dx,y+dy,dx,dy,cost+1)):
        if (nx,ny) not in grid:
            continue
        np = (nx,ny,ndx,ndy)
        s = seen.get(np)
        if s and nc > s[0]:
            continue
           
        rest = abs(fx-nx) + abs(fy-ny) + (1000 if dy==1 or dx == -1 else 0)
        d = (nc+rest, np, nc, pose)
        bisect.insort(q, d, key=lambda x: x[0])
        


print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

q = list(nodes)
nodes = set()
while len(q):
    pose = q.pop()
    nodes.add((pose[0],pose[1]))
    _, prev = seen[pose]
    for p in prev:
        if p:
            q.append(p)


if False:
    for y in range(ymax):
        l = ""
        for x in range(xmax):
            if (x,y) not in grid:
                l += ' '
            else:   
                if (x,y) in nodes:
                    l += "O"
                else:
                    l += "."
        print(l)

res = len(nodes)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
