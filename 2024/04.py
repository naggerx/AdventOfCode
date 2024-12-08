import sys, re
from pathlib import Path

with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.readlines()

maxy = len(lines)
maxx = len(lines[0])-1

res = 0

def find_directed(map, posx, posy, dirx, diry):
    word = "MAS"
    if  not (0 <= posy + diry * len(word) < maxy):
        return 0
    if  not (0 <= posx + dirx * len(word) < maxx):
        return 0
    for ch in word:
        posx += dirx
        posy += diry
        if map[posy][posx] != ch:
            return 0
    return 1

for y in range(maxy):
    for x in range(maxx):
        if lines[y][x] == 'X':
            res += find_directed(lines, x, y,  1,  0)
            res += find_directed(lines, x, y,  0,  1)
            res += find_directed(lines, x, y,  0, -1)
            res += find_directed(lines, x, y, -1,  0)
            res += find_directed(lines, x, y,  1,  1)
            res += find_directed(lines, x, y, -1, -1)
            res += find_directed(lines, x, y,  1, -1)
            res += find_directed(lines, x, y, -1,  1)

print("Part1:", res)



def find_pattern(map, posx, posy, word):
    if map[posy - 1][posx - 1] != word[0]:
        return 0
    if map[posy - 1][posx + 1] != word[1]:
        return 0
    if map[posy + 1][posx - 1] != word[2]:
        return 0
    if map[posy + 1][posx + 1] != word[3]:
        return 0
    return 1

res = 0
for y in range(1,maxy-1):
    for x in range(1, maxx-1):
        if lines[y][x] == 'A':
            res += find_pattern(lines, x, y, "MSMS")
            res += find_pattern(lines, x, y, "SSMM")
            res += find_pattern(lines, x, y, "MMSS")
            res += find_pattern(lines, x, y, "SMSM")

print("Part2:", res)
print()