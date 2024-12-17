import sys, re, time, itertools, functools
from pathlib import Path
starttime = time.time()

with open(Path(__file__).stem + "_in.txt") as f:
    blocks = f.read().split('\n\n')

lines = blocks[0].split('\n')
moves = blocks[1].replace('\n', '')

ymax = len(lines)
xmax = len(lines[0])

grid = {}
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == '@':
            rx, ry = x,y
        elif c != '.':
            grid[x,y] = c

dirs = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}

def boxmove(x,y, dx,dy):
    nx,ny = x+dx,y+dy
    c = grid.get((nx,ny))
    if c == '#':
        return False
    elif c == 'O':
        if boxmove(nx,ny, dx,dy):
            del(grid[x,y])
            grid[nx,ny] = 'O'
            return True
        return False
    else:
        del(grid[x,y])
        grid[nx,ny] = 'O'
        return True
        
for m in moves:
    nx,ny = rx+dirs[m][0],ry+dirs[m][1]
    c = grid.get((nx,ny))
    if c == '#':
        continue
    elif c == 'O':
        if not boxmove(nx,ny, dirs[m][0],dirs[m][1]):
            continue
    rx,ry = nx,ny

#print('\n'.join([''.join([(grid.get((x,y)) or ' ') for x in range(xmax)]) for y in range(ymax)]))
res = sum(100 * y + x for (x,y),c in grid.items() if c == 'O')
print(f"Part1: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()


ymax = len(lines)
xmax = len(lines[0] * 2)

grid = {}
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == '@':
            rx, ry = x*2,y
        elif c != '.':
            grid[(x*2+0,y)] = {'O': '[', '#': '#'}[c]
            grid[(x*2+1,y)] = {'O': ']', '#': '#'}[c]
#print('\n'.join([''.join([(grid.get((x,y)) or ' ') for x in range(xmax)]) for y in range(ymax)]))

dirs = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}


def boxmove_updown(x,y, dx,dy):
    global grid
    nx,ny = x+dx,y+dy
    c = (grid.get((nx,ny)), grid.get((nx+1,ny)))
    free = True
    if c[0] == '#' or c[1] == '#':
        free = False
    elif c == ('[', ']'):
        free = boxmove_updown(nx,ny, dx,dy)
    elif c == (']', '['):
        safe_grid = grid.copy()
        free = boxmove_updown(nx-1,ny, dx,dy) and boxmove_updown(nx+1,ny, dx,dy)
        if not free:
            grid = safe_grid
    elif c == (']', None):
        free = boxmove_updown(nx-1,ny, dx,dy)
    elif c == (None, '['):
        free = boxmove_updown(nx+1,ny, dx,dy)
            
    if free:
        del(grid[x+0,y])
        del(grid[x+1,y])
        grid[nx+0,ny] = '['
        grid[nx+1,ny] = ']'
    return free

        
def boxmove_leftright(x,y, dx,dy, which):
    nx,ny = x+dx,y+dy
    c = grid.get((nx,ny))
    free = True
    if c == '#':
        free = False
    elif c == '[' or c == ']':
        free = boxmove_leftright(nx,ny, dx,dy, c)
    if free:
        del(grid[x,y])
        grid[nx,ny] = which
    return free


for m in moves:
    nx,ny = rx+dirs[m][0],ry+dirs[m][1]
    c = grid.get((nx,ny))
    free = True
    if c == '#':
        free = False
    elif c == '[' or c == ']':
        if dirs[m][1] == 0:
            free = boxmove_leftright(nx,ny, dirs[m][0],dirs[m][1], c)
        else:
            free = boxmove_updown(nx if c=='[' else nx-1,ny, dirs[m][0],dirs[m][1])
    if free:
        rx,ry = nx,ny

#print('\n'.join([''.join([(grid.get((x,y)) or ' ') for x in range(xmax)]) for y in range(ymax)]))
res = sum(100 * y + x for (x,y),c in grid.items() if c == '[')
print(f"Part2: {res}  ({time.time()-starttime:.3}s)")
starttime = time.time()
