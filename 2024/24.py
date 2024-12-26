import sys, re, time, itertools, functools, heapq, collections, random
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    inputs,expr = f.read().split('\n\n')

v = {}
for line in inputs.split('\n'):
    var, val = line.split(': ')
    v[var] = int(val)

res = 0
while True:
    all_results = True
    for line in expr.split('\n'):
        o1,op,o2,_, var = line.split(' ')
        if o1 not in v or o2 not in v:
            all_results = False
            continue
        if op == 'XOR':
            v[var] = v[o1] ^ v[o2]
        elif op == 'AND':
            v[var] = v[o1] and v[o2]
        elif op == 'OR':
            v[var] = v[o1] or v[o2]
            
        if var[0] == 'z' and v[var] == 1:
            res |= (1 << int(var[1:]))

    if all_results:
        break


print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


ops = {}
for line in expr.split('\n'):
    o1,op,o2,_, var = line.split(' ')
    ops[var] = (o1,op,o2)

    

def calc_names(var, ops):
    if var[0] in "xy":
        return []
    o1,op,o2 = ops[var]
    return [var] + calc_names(o1, ops) + calc_names(o2, ops)


def test_bit(bit, myops):
    class MySeenException(Exception):
        pass

    def calc(var):
        if var[0] == 'x':
            return (x >> int(var[1:])) & 1
        if var[0] == 'y':
            return (y >> int(var[1:])) & 1
        if var in seen:
            raise MySeenException(var)
        seen.add(var)
        o1,op,o2 = myops[var]
        #print("c", var, o1, o2, seen)
        v1 = calc(o1)
        v2 = calc(o2)
        if op == 'XOR':
            return v1 ^ v2
        elif op == 'AND':
            return v1 & v2
        elif op == 'OR':
            return v1 | v2

    z = f'z{bit:02}'
    for j in range(16):
        x = random.randint(0, 1<<45)
        y = random.randint(0, 1<<45)
        seen = set()
        try:
            a = calc(z)
        except MySeenException:
            return False
        b = ((x+y) >> i) & 1
        if a != b:
            return False
    return True
    
names = set(ops.keys())
good = set()
swaps = set()
for i in range(46):
    
    if test_bit(i, ops):
        good |= set(calc_names(f'z{i:02}', ops))
        print(f"Bit {i:2}: Good  {len(good)}/{len(names)}")
        continue

    bad = set(calc_names(f'z{i:02}', ops)).difference(good)
    print(f"Bit {i:2}: Bad:  1 of ({bad}); 2 of {len(names.difference(good))}")

    bad = names.difference(good)
    for v1,v2 in itertools.combinations(bad, 2):
        o = ops.copy()
        o[v1], o[v2] = o[v2], o[v1]
        if test_bit(i, o):
            print(f"              Fixed by swap {v1} <-> {v2}")
            swaps |= {v1,v2}
            ops = o
            good |= set(calc_names(f'z{i:02}', ops))
            break
    else:
        print(f"Bit {i:2}: No swap found")
        raise()
        
res = ','.join(sorted(swaps))
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
