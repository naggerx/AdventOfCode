import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split(',')


res = 0
for line in lines:
    start,stop = map(int, line.split('-'))
    for id in range(start, stop + 1):
        s = str(id)
        if s[0:len(s)//2] == s[len(s)//2:]:
            #print(s, len(s)//2)
            res += id


print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


res = 0
for line in lines:
    start,stop = map(int, line.split('-'))
    for id in range(start, stop + 1):
        s = str(id)
        for n in range(1, len(s)//2+1):
            p0 = s[0:n]
            if all(p0 == x for x in (s[i:i+n] for i in range(n, len(s), n))):
                #print(s, n, parts)
                res += id
                break


print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
