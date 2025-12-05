import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    ranges,ids = f.read().split('\n\n')

fresh = [tuple(map(int, r.split('-'))) for r in ranges.split('\n')]

res = 0
for id in ids.split('\n'):
    for a,b in fresh:
        if a <= int(id) <= b:
            res += 1
            break          

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


res = 0
fresh.sort()
aa,bb = fresh[0]
for a,b in fresh[1:]:  
    if a > bb: # new range
        res += bb - aa + 1
        aa, bb = a,b           
    elif b > bb: # extend range
        bb = b
    else: # within range
        pass 
res += bb - aa + 1

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
