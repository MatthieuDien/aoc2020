from itertools import product

l = []

with open("input-1","r") as f:
    for line in f:
        l.append(int(line[:-1]))

for a,b in product(l, repeat=2):
    if a + b == 2020:
        print(f"{a} + {b} == 2020")
        print(f"{a} * {b} == {a*b}")
        break

for a,b,c in product(l, repeat=3):
    if a + b + c == 2020:
        print(f"{a} + {b} + {c} == 2020")
        print(f"{a} * {b} * {c} == {a*b*c}")
        break
