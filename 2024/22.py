import sys, time, collections
from collections import defaultdict as dd
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

res = 0
diffs = {}
for line in lines:
    num = int(line)
    for j in range(2000):
        num = ((num * 64) ^ num) % 16777216       
        num = ((num // 32) ^ num) % 16777216       
        num = ((num * 2048) ^ num) % 16777216
    res += num

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

prices = dd(int)
for line in lines:
    num = int(line)
    seen = set()
    changes = collections.deque(maxlen = 4)
    for _ in range(2000):
        last_price = num % 10
        num = ((num * 64) ^ num) % 16777216       
        num = ((num // 32) ^ num) % 16777216       
        num = ((num * 2048) ^ num) % 16777216
        changes.append(num % 10 - last_price)
        d = tuple(changes)
        if d not in seen:
            seen.add(d)
            prices[d] += num % 10

res =  max(prices.values())
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
