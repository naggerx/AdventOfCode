import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')


res = 0
for line in lines:
    values = [int(i) for i in line]
    v0 = max(values[:-1])
    v1 = max(values[values.index(v0)+1:])
    #print(values, v0 * 10 + v1)
    res += v0 * 10 + v1


print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


def max_with_index(l):
    m = max(l)
    return (m, l.index(m))

res = 0
for line in lines:
    values = [int(i) for i in line]
    #print(values)
    jolts = 0
    i0 = 0
    for n in range(12, 0, -1):
        v, i = max_with_index(values[i0:len(values)-n+1])
        jolts = jolts * 10 + v
        #print(f"  {n}: l[{i0}:{len(values)-n+1}]: {values[i0:len(values)-n+1]} -> max: {v},  idx: {i}({i0+i})  j:{jolts}")
        i0 += i + 1
    res += jolts


print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
