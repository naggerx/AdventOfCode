import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in0.txt") as f:
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


groups = set()
for y,line in enumerate(lines):
    c1,c2 = line.split('-')
    #print("=====", y, len(lines), c1,c2)

    groups_new = set()
    num_used = 0
    while groups:
        g = groups.pop()
        s = set()
        if c1 in g or all(gi in seen[c1] for gi in g):
            s.add(c1)
        if c2 in g or all(gi in seen[c2] for gi in g):
            s.add(c2)
        if s:
            groups_new.add(frozenset(g | s))
            num_used += 1            
        else:
            groups_new.add(g)
           
    if num_used == 0:
        groups_new.add(frozenset({c1,c2}))
    groups = groups_new
    
    
for g in groups:
    print("  +", g)
res = ','.join(sorted(max(groups, key=len)))
print((len(res)+1)//3)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
