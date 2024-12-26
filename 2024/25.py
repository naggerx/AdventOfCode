import sys, re, time, itertools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    blocks = f.read().split('\n\n')


keys, locks = [], []
for b in blocks:
    p = [-1] * 5
    for y,line in enumerate(b.split('\n')):
        for x,c in enumerate(line):
            p[x] += (c == '#')
    if b[0]=='#':
        locks.append(p)
    else:
        keys.append(p)
        
#print(locks)
#print(keys)
                

res = sum(all(ll+kk <=5 for ll,kk in zip(l,k)) for l,k in itertools.product(locks, keys))

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

