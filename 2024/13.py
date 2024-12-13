import sys, re, time, itertools, functools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    chunks = f.read().split('\n\n')

equ = []
for c in chunks:
    equ.append(list(map(int,re.findall(r'\d+', c, flags = re.DOTALL))))
    

#print(equ)    
res = 0
for ax,ay,bx,by,sx,sy in equ:    
    for a in range(100):
        for b in range(100):
            if a*ax + b*bx ==sx and a*ay + b*by == sy:
                res += 3*a + b
                break
        else:
            continue
        break
        

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


for e in equ:
    e[4] += 10000000000000
    e[5] += 10000000000000

res = 0
for ax,ay,bx,by,sx,sy in equ:
    an = sx*by - sy*bx
    ad = ax*by - ay*bx
    if an % ad != 0:
        #print(f"  ", sx, sy, an % ad)
        continue
    a = an // ad
    b = (sy - a * ay) // by
    #print(f"  ", sx, sy, an % ad, a, b, a*ax + b*bx - sx, a*ay + b*by - sy, 3*a, b)
    
    res += 3*a + b


print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
