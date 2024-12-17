import sys, re, time, itertools, functools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

if len(lines) < 20:
    ymax = 7
    xmax = 11
else:
    ymax = 103
    xmax = 101

robots = []
for line in lines:
    robots.append(list(map(int,re.findall(r'-?\d+', line))))
    
res = 0
for _ in range(100):
    for r in robots:    
        r[0] = (r[0] + r[2]) % xmax
        r[1] = (r[1] + r[3]) % ymax

res = 1
for o1,o2 in ((-1,1),(1,1),(1,-1),(-1,-1)):   
    q = len([1 for r in robots if o1 * r[0] > o1 * (xmax//2) and o2 * r[1] > o2 * (ymax//2)])
    print(q)
    res *= q

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


robots = []
for line in lines:
    robots.append(list(map(int,re.findall(r'-?\d+', line))))

for res in range(1,1000000):    
    
    for r in robots:    
        r[0] = (r[0] + r[2]) % xmax
        r[1] = (r[1] + r[3]) % ymax

    if res == 7492:  # s % 101 == 18:

        for y in range(ymax):
            line = ""
            for x in range(xmax):
                n = len([1 for r in robots if x == r[0] and y == r[1]])
                line += str(n) if n>0 else ' '
            print(line)
        #print("step", res)
        break #input()

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
