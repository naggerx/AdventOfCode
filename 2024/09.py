import sys, re, time
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    line = f.read().strip()


disk=[]
for i,l in enumerate(map(int,line)):
    disk += [-1 if i%2 else i//2 ] * l

res = 0
j = len(disk) - 1
for i in range(len(disk)):
    while disk[i] == -1:
        disk[i], disk[j], j = disk[j], -1, j-1
    if i >= j:
        break
    res += i * disk[i]

print(f"Part1: {res}  ({time.time()-starttime:.3}s)")

starttime = time.time()
files, spaces, pos = [], [], 0
POS,LEN,ID = range(3)
for i,l in enumerate(map(int,line)):
    (spaces if i%2 else files).append([pos, l, i//2])
    pos += l

for file in reversed(files):
    for space in spaces:
        if file[POS] < space[POS]:
            break
        if file[LEN] <= space[LEN]:
            file[POS] = space[POS]
            space[POS] += file[LEN]
            space[LEN] -= file[LEN]
            break

res = sum((file[POS] + i) * file[ID] for file in files for i in range(file[LEN]))
      
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
