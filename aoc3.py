fd = open("input-3","r")
forest = fd.readlines()
h, w = len(forest), len(forest[0])-1

def get(i, j):
    return forest[i][j%w]

print(sum((get(i,i) == "#" for i in range(h)))*
      sum((get(i,i*3) == "#" for i in range(h)))*
      sum((get(i,i*5) == "#" for i in range(h)))*
      sum((get(i,i*7) == "#" for i in range(h)))*
      sum((get(i,i//2) == "#" for i in range(0,h,2))))
