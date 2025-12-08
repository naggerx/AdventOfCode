import sys, re, time, itertools, functools, heapq, collections, operator
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')


ops = [{'*':operator.mul, '+':operator.add}[o] for o in lines[-1] if o != ' ']
res = sum(functools.reduce(op, v) for op,v in zip(ops, map(list,zip(*[map(int, filter(bool, l.split(' '))) for l in lines[:-1]]))))

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


res = 0
values = []
i = 0
for col in zip(*lines[:-1]):
    s = ''.join(col)
    if s.strip() != '':
        values.append(int(s))
    else:
        res += functools.reduce(ops[i], values)
        values = []
        i += 1
res += functools.reduce(ops[i], values)

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
