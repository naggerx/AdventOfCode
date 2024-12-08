import sys, re, time
from pathlib import Path

starttime = time.time()


with open(Path(__file__).stem + "_in.txt") as f:
    text = f.read()

C = len(text.split('\n',1)[0])
R = text.count('\n') + 1

text_org = text

def unoptimized():
    L = len(text.split('\n',1)[0])

    text_prev = ''
    while text != text_prev:
        text_prev = text
        text = re.sub(rf'(?:\.|X)(.{{{L}}})\^',r'^\1X', text, flags = re.DOTALL)  # go up
        text = re.sub(rf'(?<=#.{{{L}}})\^',r'>', text, flags = re.DOTALL) # rotate to >
        text = re.sub(rf'>(?:\.|X)',r'X>', text, flags = re.DOTALL)  # go right
        text = re.sub(rf'>#',r'v#', text, flags = re.DOTALL) # rotate to v
        text = re.sub(rf'v(.{{{L}}})(?:\.|X)',r'X\1v', text, flags = re.DOTALL)  # go down
        text = re.sub(rf'v(?=.{{{L}}}#)',r'<', text, flags = re.DOTALL) # rotate to <
        text = re.sub(rf'(?:\.|X)<',r'<X', text, flags = re.DOTALL)  # go left
        text = re.sub(rf'#<',r'#^', text, flags = re.DOTALL) # rotate to ^

    print(text)
    res = text.count('X')+1
    print("Part1:", res, time.time()-starttime)


r = [
    [re.compile(rf'(?:\.|\w)(.{{{C}}})\^', re.DOTALL), r'^\1A'   , re.compile(rf'(?<=#.{{{C}}})\^', re.DOTALL), r'>' , rf'>B'],  # up
    [re.compile(rf'>(?:\.|\w)'           , re.DOTALL), r'B>'     , re.compile(rf'>#'              , re.DOTALL), r'v#', rf'rewr'],  # right
    [re.compile(rf'v(.{{{C}}})(?:\.|\w)' , re.DOTALL), r'C\1v'   , re.compile(rf'v(?=.{{{C}}}#)'  , re.DOTALL), r'<' , rf'D<'],  # down
    [re.compile(rf'(?:\.|\w)<'           , re.DOTALL), r'<D'     , re.compile(rf'#<'              , re.DOTALL), r'#^', rf'werwerr'],  # left
 ]

dir = 0
for i in range(1000000):
    n = 1
    while n > 0:
        text, n = r[dir][0].subn(r[dir][1], text) # move
    text, n = r[dir][2].subn(r[dir][3], text)  # rotate
    if n > 0:        
        dir = (dir + 1) % 4
    else:
        break

for line in text.splitlines():
    print("   ", line)

res = len(re.findall('\w', text))
print("Part1:", res, time.time()-starttime)


text_path = text
res = 0
for ch_idx, ch in enumerate(text_path):
    if ch not in ['A', 'B', 'C', 'D', 'v', '>']:
        continue

    if text_org[ch_idx] == '^':
        continue

    print(ch_idx, len(text), time.time()-starttime)
    starttime = time.time()

    dir = 0
    text = text_org[:ch_idx] + '#' + text_org[ch_idx+1:]
    for i in range(300):
        n = 1
        while n > 0:
            text, n = r[dir][0].subn(r[dir][1], text) # move
        text, n = r[dir][2].subn(r[dir][3], text)  # rotate
        if n > 0:
            if m:= re.search(r[dir][4], text):
                print("loop", i)
                res += 1
                break
            dir = (dir + 1) % 4
        else:
            print('out', i)
            break
    else:
        # we cannot detect if we got stucked in a line
        res += 1
        #for line in text.splitlines():
        #    print("   ", line)

print("Part2:", res, time.time()-starttime)
