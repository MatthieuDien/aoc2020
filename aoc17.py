from collections import defaultdict
from itertools import product

grid = [defaultdict(lambda : ".")]
mx, Mx, my, My, mz, Mz = 0,0,0,0,0,1

with open("input-17","r") as f:
    for i,line in enumerate(f):
        Mx = len(line)-1
        My += 1
        for j,case in enumerate(line[:-1]):
            grid[0][(i,j,0)] = case

def sumt(t1,t2):
    return tuple(map(sum,zip(t1,t2)))

def neighbors(p, step):
    nghb = ""
    for c in product((0,1,-1), repeat=3):
        if c != (0,0,0):
            nghb += grid[step][sumt(c,p)]
    return nghb

def pprint():
    s = ""
    for k in range(mz, Mz):
        s += f"z={k}\n"
        for i in range(mx, Mx):
            for j in range(my, My):
                s += grid[-1][(i,j,k)]
            s+="\n"
        s+="\n"
    print(s)
    
for step in range(6):
    pprint()
    # print(mx, Mx, my, My, mz, Mz)
    grid.append(defaultdict(lambda : "."))
    for k in range(mz-1, Mz+1):
        for i in range(mx-1, Mx+1):
            for j in range(my-1, My+1):
                # print(k)
                p=(i,j,k)
                nghb = neighbors(p, step)
                # print(p, nghb)
                if grid[step][p] == "." and nghb.count("#") == 3:
                    grid[step+1][p] = "#"
                    mx, Mx, my, My, mz, Mz = min(i-1,mx),max(1+i,Mx),min(j-1,my),max(1+j,My),min(k-1,mz),max(k+1,Mz)
                elif grid[step][p] == "#" and 2 <= nghb.count("#") <= 3:
                    grid[step+1][p] = "#"
                else:
                    grid[step+1][p] = "."
print("".join(grid[-1].values()).count("#"))
                    
                
