import sys
from pprint import pp

with open("01_in.txt") as f:
    lines = f.readlines()

left = []
right = []
for line in lines:
    l,r = line.split('   ')
    left.append(int(l))
    right.append(int(r))
    
res = sum([abs(l-r) for l,r in zip(sorted(left), sorted(right))])   
print("Part1:", res)

res = sum(l * right.count(l) for l in left)
print("Part2:", res)
