import sage.all
from sage.arith.misc import crt
from itertools import combinations

with open("input-13","r") as f:
    l = f.readlines()
    l[0] = int(l[0][:-1])
    l[1] = l[1][:-1].split(",")

    t = l[0]
    res = 0
    s = {int(x) for x in l[1] if x != "x"}
    while res == 0:
        t += 1
        for x in s:
            if t % x == 0:
                res = x
                break
    print((t-l[0])*res)


    residues = []
    modulos = []
    for i,bus in enumerate(l[1]):
        if bus != "x":
            bus = int(bus)
            residues.append(-i+bus)
            modulos.append(bus)

    print(crt(residues, modulos))
