import sys, re, time
from pathlib import Path
starttime = time.time()


with open(Path(__file__).stem + "_in.txt") as f:
    lines = f.readlines()

res = 0
for line in lines:
    expected, values = line.split(': ')
    expected = int(expected)

    def calc(actual, rest):
        if not rest:
            return actual == expected
        v = rest.pop(0)        
        return calc(actual + v, rest.copy()) or calc(actual * v, rest.copy())

    values = list(map(int,values.split(' ')))
    actual = values.pop(0)
    if calc(actual, values.copy()):
        res += expected

print(f"Part1: {res}  ({time.time()-starttime:.2}s)")

starttime = time.time()
res = 0
for line in lines:
    expected, values = line.split(': ')
    expected = int(expected)

    def calc(actual, rest):
        if not rest:
            return actual == expected
        v = rest.pop(0)        
        return (calc(actual + v, rest.copy()) or calc(actual * v, rest.copy())
                 or calc(int(str(actual)+str(v)), rest))

    values = list(map(int,values.split(' ')))
    actual = values.pop(0)
    if calc(actual, values):
        res += expected

print(f"Part2: {res}  ({time.time()-starttime:.2}s)")
