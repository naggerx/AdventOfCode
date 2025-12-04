import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in0.txt") as f:
    lines = f.read().split('\n')
    block,lines = f.read().split('\n\n')

moves = block.replace("\n", "")
stones = list(map(int,lines.split(' ')))


ymax = len(lines)
xmax = len(lines[0])

if len(lines) > 50:
    xmax = 71
    num_part1 = 1024
else:
    xmax = 7
    num_part1 = 12
ymax = xmax

#block input
#a,b,c = list(map(int,re.findall(r'-?\d+', block, flags = re.DOTALL))))

robots = []
for line in lines:
    #a,x,y = list(map(int,re.findall(r'-?\d+', line))))
    #vals = list(map(int,line.split(' ')))


sx,sy = 0,0
ex,ey = xmax-1,ymax-1

walls = {}
walls = set()
for y,line in enumerate(lines):

    #coordinates in input
    gx,gy = map(int,re.findall(r'-?\d+', line))
    walls.add((gx,gy))

    #walls input store in dict
    for x,c in enumerate(line):
        if c == '@':
            sx,sy = x,y
        elif c != '.':
            walls[x,y] = c

    #walls input store in set
    for x,c in enumerate(line):
        if c in 'SE.':
            walls.add((x,y))
            if c == 'S':
                sx,sy = x,y

#print walls as dict
print('\n'.join([''.join([(walls.get((x,y)) or ' ') for x in range(xmax)]) for y in range(ymax)]))
#print walls as set
print('\n'.join([''.join([('#' if (x,y) in walls else ' ') for x in range(xmax)]) for y in range(ymax)]))
#print walls and costs (seen)
print('\n'.join([''.join([('###' if (x,y) in walls else (f"{seen[x,y]%100:^3}" if (x,y) in seen else '   ')) for x in range(xmax)]) for y in range(ymax)]))
#print walls as set and costs (seen)
print('\n'.join([''.join([('###' if (x,y) in walls else (f"{seen[x,y]%100:^3}" if (x,y) in seen else '   ')) for x in range(xmax)]) for y in range(ymax)]))
#print walls complicated
if False:
    for y in range(ymax):
        line = ""
        for x in range(xmax):
            n = len([1 for r in robots if x == r[0] and y == r[1]])
            line += str(n) if n>0 else ' '
        print(line)


adj4 = ((0,-1), (0,1), (-1,0), (1,0))
adj8 = ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1))
dirs = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}




#find segments
seen = set()
res = 0
for y0,line in enumerate(lines):
    for x0,c0 in enumerate(line):
        if (x0,y0) in seen:
            continue

        region = [(x0,y0)]
        while region:        
            x,y = region.pop()
            if (x,y) in seen:
                continue
            seen.add((x,y))
            for dx,dy in adj4:
                nx,ny = x+dx, y+dy
                if 0 <= nx < xmax and 0 <= ny < ymax:
                    if lines[ny][nx] == c0:
                        region.append((xx,yy))
                
                if nx < 0 or nx >= xmax or ny < 0 or ny >= ymax:
                    fences += 1
                elif lines[ny][nx] != c0:
                    fences += 1
                else:
                    region.append((xx,yy))




#dijkstra with path
seen = {(sx,sy):0}
q = [(0, sx,sy, [(sx,sy)])]
while len(q):
    c,x,y,path = heapq.heappop(q)
    if (x,y) == (ex,ey):
        print("found with cost", c)
        #print('\n'.join([''.join([('###' if (x,y) in walls else (f"{seen[x,y]%100:^3}" if (x,y) in seen else '   ')) for x in range(xmax)]) for y in range(ymax)]))
        res = c
        break
    for dx,dy in adj4:
        nc, nx, ny = c+1, x+dx, y+dy
        if (nx,ny) not in walls and 0 <= nx < xmax and 0 <= ny < ymax:
            if nc < seen.get((nx,ny), 100000):
                seen[nx,ny] = nc
                heapq.heappush(q, (nc,nx,ny, path + [(nx,ny)]))
else:
    print("no path found")



print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


#res = 0
#for line in lines:


#print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
