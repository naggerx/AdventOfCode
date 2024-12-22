import sys, re, time, itertools, functools, heapq, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')


numpad_pos = {'7': (0,0), '8': (1,0), '9':(2,0), '4':(0,1), '5':(1,1), '6':(2,1), '1':(0,2), '2':(1,2), '3':(2,2), '0':(1,3) ,'A':(2,3)}
numpad_seq = dd(set)
for i,(x1,y1) in numpad_pos.items():
    for j,(x2,y2) in numpad_pos.items():
        s = ">" * (x2-x1) + "v" * (y2-y1) + "^" * (y1-y2) + "<" * (x1-x2)       
        for s in (''.join(i) for i in itertools.permutations(s)):
            if i=='0' and s[:1]=='<':
                continue
            if i=='A' and s[:2]=='<<':
                continue
            if j=='0' and s[-1:]=='>':
                continue
            if j=='A' and s[-2:]=='>>':
                continue
            numpad_seq[(i,j)].add(s+'A')


keypad_pos = {'^': (1,0), 'A':(2,0), '<':(0,1), 'v':(1,1), '>':(2,1)}
keypad_seq = dd(set)
for i,(x1,y1) in keypad_pos.items():
    for j,(x2,y2) in keypad_pos.items():
        s = "v" * (y2-y1) + ">" * (x2-x1) + "<" * (x1-x2) + "^" * (y1-y2)
        for s in (''.join(i) for i in itertools.permutations(s)):
            if i=='<' and s[:1]=='^':
                continue
            if j=='<' and s[-1:]=='v':
                continue
            keypad_seq[(i,j)].add(s+'A')


@functools.cache
def expand_seq(is_first, level, seq):
    if level == 0:
        return seq       
    expanded = ""
    for c1,c2 in itertools.pairwise('A'+seq):
        subseq = numpad_seq[c1,c2] if is_first else keypad_seq[c1,c2]
        expanded += min((expand_seq(False, level-1, s) for s in subseq), key=len)
    return expanded

@functools.cache
def expand_costs(is_first, level, seq):
    if level == 0:
        return len(seq)        
    l = 0
    for c1,c2 in itertools.pairwise('A'+seq):
        subseq = numpad_seq[c1,c2] if is_first else keypad_seq[c1,c2]
        l += min(expand_costs(False, level-1, s) for s in subseq)
    return l
    

res = 0
for line in lines[:]:
    c = expand_seq(True, 2 + 1, line[:])
    print(line + ":", len(c), c)
    res += int(line[:3]) * len(c)
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
print()

res = 0
for line in lines[:]:
    l = expand_costs(True, 25 + 1, line[:])   
    print(line + ":", l)
    res += int(line[:3]) * l
    
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
#starttime = time.time()
