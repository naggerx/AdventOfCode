import sys, re, time, functools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    block1,block2 = f.read().split('\n\n')

re1 = re.compile("(" + block1.replace(', ','|') + ")+")
res = sum(re1.fullmatch(line) is not None for line in block2.split('\n'))
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

towels = block1.split(", ")
lines = block2.split('\n')

@functools.cache
def dfs(rest):
    return sum(1 if rest == t else dfs(rest[len(t):]) for t in towels if rest.startswith(t))
    #num = 0
    #for t in towels:
    #    if rest.startswith(t):
    #        if rest == t:
    #            num += 1
    #        else:
    #            num += dfs(rest[len(t):])
    #return num
    
res = sum(dfs(line) for line in lines)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
