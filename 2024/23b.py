import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

res = 0
seen = dd(list)
for y,line in enumerate(lines):
    c1,c2 = line.split('-')
    seen[c1].append(c2)
    seen[c2].append(c1)
        
for c1,cs in seen.items():
    for c2,c3 in itertools.combinations(cs, 2):
        if c3 in seen[c2]:
            for c in [c1,c2,c3]:
                if c.startswith('t'):
                    res += 1
                    break
res //= 3
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


res = 0
groups = set()
for y,line in enumerate(lines):
    c1,c2 = line.split('-')

    groups_new = set()
    to_remove = []
    #print("=====", y, len(lines), c1,c2)
    for g in groups:
        if c1 in g:
            if c2 in g:
                continue
            else:
                if all(gi in seen[c2] for gi in g):
                    to_remove.append(g)
                    groups_new.add(tuple(sorted(g + (c2,))))
        else:
            if c2 in g:
                if all(gi in seen[c1] for gi in g):
                    to_remove.append(g)
                    groups_new.add(tuple(sorted(g + (c1,))))
            else:
                if all(gi in seen[c1] for gi in g) and all(gi in seen[c2] for gi in g):
                    to_remove.append(g)
                    groups_new.add(tuple(sorted(g + (c1,c2))))

    for g in to_remove:
        groups.remove(g)
    for g in groups_new:
        groups.add(g)
    groups.add(tuple(sorted([c1,c2])))
    
    
#for g in groups:
#    if len(g) > 5:
#        print("  +", g)
res = ','.join(max(groups, key=len))
print((len(res)+1)//3)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
