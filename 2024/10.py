import sys, re, time, itertools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in0.txt") as f:
    lines = f.read().split('\n')

area = {(x,y):int(c) for y,line in enumerate(lines) for x,c in enumerate(line)}


def step(pos, exp_height, seen):       
    h = area.get(pos)
    if h == exp_height:
        if h == 9:
            seen.add(pos)
        else:
            for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
                step((pos[0] + dx, pos[1] + dy), exp_height + 1, seen)
    
res = 0
for pos in area:
    seen = set()
    step(pos, 0, seen)
    res += len(seen)

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


# Step2: exactly like Step1, but with 'seen' as list

def step(pos, exp_height, seen):       
    h = area.get(pos)
    if h == exp_height:
        if h == 9:
            seen.append(pos)
        else:
            for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
                step((pos[0] + dx, pos[1] + dy), exp_height + 1, seen)
    
res = 0
seen = []
for pos in area:
    step(pos, 0, seen)
res += len(seen)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


#Alternative Step2

def step(pos, exp_height):
    h = area.get(pos)
    if h != exp_height:
        return 0
    elif h == 9:
        return 1
    sum = 0
    for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
        sum += step((pos[0] + dx, pos[1] + dy), exp_height + 1)
    return sum

res = 0
for pos in area:
    res += step(pos, 0)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


#Condensed Alternative Step2

def step(pos, exp_height):
    h = area.get(pos)
    if h != exp_height:
        return 0
    elif h == 9:
        return 1
    return sum(step((pos[0] + dx, pos[1] + dy), exp_height + 1) for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)))

res = sum(step(pos, 0) for pos in area)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
