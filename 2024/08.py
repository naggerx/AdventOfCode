import sys, re, time, itertools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.read().split('\n')

ymax = len(lines)
xmax = len(lines[0])

chars = {}
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c not in ['.']:
            chars.setdefault(c, []).append((x,y))


antinodes = set()
for ch,locations in chars.items():
    for (x1,y1),(x2,y2) in itertools.combinations(locations, 2):
        for x,y in ((2 * x1 - x2, 2 * y1 - y2), (2 * x2 - x1, 2 * y2 - y1)):
            if 0 <= x < xmax and 0 <= y < ymax:
                antinodes.add((x,y))

res = len(antinodes)
print(f"Part1: {res}  ({time.time()-starttime}s)")

# -----------------------------
starttime = time.time()
antinodes = set()
for ch,locations in chars.items():
    for (x1,y1),(x2,y2) in itertools.combinations(locations, 2):
        for dir in (-1,1):
            for i in range(xmax):
                x,y = x1 + dir * i * (x2 - x1), y1 + dir * i * (y2 - y1)
                if 0 <= x < xmax and 0 <= y < ymax:
                    antinodes.add((x,y))
                else:
                    break

res = len(antinodes)
print(f"Part2: {res}  ({time.time()-starttime}s)")

# -----------------------------
starttime = time.time()
antinodes = set()
for ch,locations in chars.items():
    for (x1,y1),(x2,y2) in itertools.permutations(locations, 2):
        for i in range(xmax):
            x,y = x1 + dir * i * (x2 - x1), y1 + dir * i * (y2 - y1)
            if 0 <= x < xmax and 0 <= y < ymax:
                antinodes.add((x,y))
            else:
                break

res = len(antinodes)
print(f"Part2: {res}  ({time.time()-starttime}s)")

# -----------------------------
starttime = time.time()
antinodes = set()
for ch,locations in chars.items():
    for (x1,y1),(x2,y2) in itertools.permutations(locations, 2):
        def in_grid(pos): return 0 <= pos[0] < xmax and 0 <= pos[1] < ymax
        antinodes.update(itertools.takewhile(in_grid, ( (x1 + i * (x2-x1), y1 + i * (y2-y1)) for i in range(xmax))))

res = len(antinodes)
print(f"Part2: {res}  ({time.time()-starttime}s)")
