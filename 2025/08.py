import sys, re, time, itertools, functools, heapq, collections, bisect, math
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')


boxes = [ tuple(map(int, f.split(','))) for f in lines ]
L = len(boxes)

max_connections = 10 if L <= 50 else 1000  # is test input


shortest = []
for i in range(L):
    for j in range(i+1,L):
        d = sum((aa-bb)**2 for aa, bb in zip(boxes[i],boxes[j]))
        if len(shortest) < 7000:
            bisect.insort(shortest, (d,i,j))
        elif d < shortest[-1][0]:
            del shortest[-1]
            bisect.insort(shortest, (d,i,j))

print(f"Calculated {len(shortest)}th shortes pathes  ({time.time()-starttime:.3}s)")


res = res2 = 0
curcuits = [{b} for b in range(len(boxes))]

for n, (_,b1,b2) in enumerate(shortest):
    c1i = next((idx for idx,v in enumerate(curcuits) if b1 in v))
    c2i = next((idx for idx,v in enumerate(curcuits) if b2 in v))
    if c1i != c2i:
        curcuits[c1i] |= curcuits[c2i]
        del curcuits[c2i]

    if n == max_connections:
        res = math.prod(sorted([len(c) for c in curcuits], reverse = True)[0:3])
    if len(curcuits) == 1:
        print(f"Finished after {n} connections")
        res2 = boxes[b1][0] * boxes[b2][0]
        break

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
print(f"Part2: {res2}  ({time.time()-starttime:.3}s)")
