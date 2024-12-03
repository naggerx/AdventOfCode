import sys, re

with open("03_in.txt") as f:
    lines = f.readlines()


res = 0
for line in lines:
    res += sum(int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', line))

print("Part1:", res)


res = 0
do = 1
for line in lines:
    m_all = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line)
    for m,x,y in m_all:
        if m[0] == 'm':
            res += int(x) * int(y) * do
        else:
            do = 1 if m[2] == '(' else 0

print("Part2:", res)
