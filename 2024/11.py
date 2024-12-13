import sys, re, time, functools
from pathlib import Path

starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')
stones = list(map(int,lines[0].split(' ')))

for step in range(25):
    starttime = time.time()
    stones_next = []
    for st in stones:
        if st == 0:
            stones_next.append(1)
        elif (l:=len(s:=str(st))) % 2 == 0:
            stones_next += [int(s[:l//2]), int(s[l//2:])]
        else:
            stones_next.append(st * 2024)
    stones = stones_next

res = len(stones)
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


stones = list(map(int,lines[0].split(' ')))

@functools.lru_cache(maxsize=None)
def count_stones(i, st):
    if i==0:
        return 1;
    if st == 0:
        return count_stones(i-1, 1)
    if len(s := str(st)) % 2 == 0:
        return count_stones(i-1, int(s[:len(s)//2])) + count_stones(i-1, int(s[len(s)//2:]))
    return count_stones(i-1, st * 2024)

res = sum(count_stones(75, st) for st in stones)
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
