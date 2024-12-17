import sys, re, time, itertools, functools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    block,lines = f.read().split('\n\n')

ax0,bx0,cx0 = list(map(int,re.findall(r'-?\d+', block, flags = re.DOTALL)))
p = list(map(int,re.findall(r'-?\d+', lines)))

print(ax0,bx0,cx0)
print(p)

def run(ax,bx,cx):

    o = []
    i = 0
    def op2(op):
        return op if op <= 3 else (ax,bx,cx)[op-4]
    
    while i<len(p):
        cmd = p[i]
        op = p[i+1]
        i += 2
        if cmd == 0:
            ax >>= op2(op)  # ax // (2**op2(op))
        elif cmd == 1:
            bx ^= op
        elif cmd == 2:
            bx = op2(op) % 8
        elif cmd == 3:
            if ax != 0:
                i = op
        elif cmd == 4:
            bx ^= cx
        elif cmd == 5:
            o.append(op2(op) % 8)
        elif cmd == 6:
            bx = ax >> op2(op)
        elif cmd == 7:
            cx = ax >> op2(op)
    return o


o = run(ax0,bx0,cx0)
res = ",".join(map(str,o))
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

"""
 p = [2, 4, 1, 1, 7, 5, 1, 5, 4, 3, 0, 3, 5, 5, 3, 0]
 2,4:  bx = ax % 8         -> bx 0..7
 1,1:  bx = bx ^ 1         -> bx 0..7
 7,5:  cx = ax >> bx       -> current output only depends max on last (7+3)bits of ax
 1,5:  bx = bx ^ 5
 4,3:  bx = bx ^ cx 
 0,3:  ax = ax >> 3        -> only expr that changes ax; every cycle 3bits less
 5,5:  out bx % 8          -> one output per cycle
 3,0:  if ax != 0: jmp 0   -> output of length 16 -> 16 cycles -> 8^16 >= ax < 8^17

   out bx % 8
   out (bx ^ cx) % 8
   out ((bx ^ 5) ^ cx) % 8
   out ((bx ^ 5) ^ (ax >> bx)) % 8
   out (((bx ^ 1) ^ 5) ^ (ax >> (bx ^ 1))) % 8
   out ((((ax % 8) ^ 1) ^ 5) ^ (ax >> ((ax % 8) ^ 1))) % 8

   out ((((ax % 8) ^ 4) ^ (ax >> ((ax % 8) ^ 1))) % 8

   msb defines last output; lsb defines first output
"""


v = [0]*16
for i in range(0,14):  # brute forcing the last 3 outputs
    for j in range(8*8*8):
        v[i] = j // 64  # lsb first, so the first match will be the smallest number
        v[i+1] = (j % 64) // 8
        v[i+2] = j % 8
        
        ax = functools.reduce(lambda x,y: x*8+y, v)
        o = run(ax,bx0,cx0)
        #print(" +", v, o, p, ax)
        if len(o) == len(p) and o[15-i] == p[15-i] and o[14-i] == p[14-i] and o[13-i] == p[13-i]:
            #print(" =", i, j,(v[i],v[i+1]), v, o, p, ax)
            res = ax
            break
        
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


q = [0]
while q:
    a = q.pop()
    for ax in range(a,a + 8):  # non-reversed: find the smallest solution at last
        o = run(ax, bx0, cx0)
        if o == p:
            res = ax
        if o == p[-len(o):]:
            q.append(ax * 8)

print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()

