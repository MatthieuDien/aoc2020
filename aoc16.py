from itertools import chain
from functools import reduce
from collections import defaultdict

with open("input-16","r") as f:
    lines = f.readlines()
    i = 0
    constraints = dict()
    while lines[i] != "\n":
        ranges = lines[i][:-1].split(": ")[1].split(" or ")
        c_name = lines[i][:-1].split(": ")[0]
        constraints[c_name] = list()
        for r in ranges:
            r1, r2 = map(int, r.split("-"))
            # print(c_name,r1,r2)
            constraints[c_name].append(set(range(r1,r2+1)))
        i+=1
    my_ticket = list(map(int,lines[i+2][:-1].split(",")))
    i += 5
    r = 0
    valid_tickets = []
    while i < len(lines):
        ticket = list(map(int,lines[i][:-1].split(",")))
        valid = True
        for v in ticket:
            if all(map(lambda c: v not in c, chain(*constraints.values()))):
                r += v
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)
        i+=1
    # Part 1
    print(r)
    # Part 2
    print(my_ticket)
    assoc = defaultdict(set)
    i = 0
    for i in range(len(my_ticket)):
        for c in constraints.keys():
            print(i, c)
            if all(map(lambda x: reduce(lambda acc, r: acc | (x in r), constraints[c], False),
                       [t[i] for t in valid_tickets])):
                assoc[c].add(i)
    print(assoc)

    while not all(map(lambda x: len(x) == 1, assoc.values())):
        singletons = set(filter(lambda x: len(assoc[x]) == 1,assoc.keys()))
        for k in singletons:
            for kk in assoc:
                if k != kk:
                    assoc[kk] -= assoc[k]
    print(assoc)    
    r = 1
    for c in assoc:
        if c.startswith("departure"):
            r *= my_ticket[assoc[c].pop()]
    print(r)
                    
