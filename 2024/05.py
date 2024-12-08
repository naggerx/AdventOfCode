import sys, re
from pathlib import Path

with open(Path(__file__).stem + "_in.txt") as f:
    all = f.read()
    
part1, part2 = all.split('\n\n')

deps = {}
for line in part1.split('\n'):
    a,b = map(int,line.split("|"))
    deps.setdefault(b, []).append(a)
    
#print(deps)
res = 0
for line in part2.split('\n'):
    pages = list(map(int,line.split(",")))
    #print("====", pages)
    for i,page in enumerate(pages):
        if page in deps:
            for dep in deps[page]:
                if dep in pages[i+1:]:
                    break
            else:
                continue
            break
    else:
        res += pages[len(pages)//2]
    
print("Part1:", res)
    
res = 0
for line in part2.split('\n'):
    pages = list(map(int,line.split(",")))
    #print("====", pages)
    pages_new = []
    pages_rest = pages.copy()
    
    while pages_rest:
        page = pages_rest.pop(0)
        #print("==", pages_new, page, pages_rest)
        failed = False
        if page not in deps:
            pages_new.append(page)
        else:
            for dep in deps[page]:
                for pr in pages_rest:
                    if dep == pr:
                        #print(page, dep, pr, pages[i+1:], pages_new, pages_rest)
                        failed = True
                        pages_rest.remove(dep)
                        pages_rest.insert(0, page)
                        pages_rest.insert(0, dep)
                        break
                if failed:
                    break
            else:
                pages_new.append(page)
            
    #print("->", pages, pages_new)
    if pages != pages_new:
        res += pages_new[len(pages)//2]

print("Part2:", res)
