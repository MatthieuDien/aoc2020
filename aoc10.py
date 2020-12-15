from sage.all import DiGraph
from collections import Counter

with open("input-10","r") as f:
    l = [int(s[:-1]) for s in f]
    m = max(l) + 3
    l.append(m)
    l.append(0)
    l = sorted(l)

    # Part 1
    d = [0,0,0,0]
    for i in range(1,len(l)):
        d[l[i]-l[i-1]] += 1
    print(d[1]*d[3])

    
    # Part 2
    d = DiGraph()
    for i in range(1,len(l)):
        for j in range(max(0,i-3),i):
            if l[i]-l[j] <= 3:
                d.add_edge(l[j], l[i])

    counter = Counter({0 : 1})
    todo = [0]
    visited = set()
    to_visit = {0}
    while todo:
        v = todo.pop()
        visited.add(v)
        neighbors = sorted(list(d.neighbors_out(v)))
        for u in neighbors:
            counter[u] += counter[v]
            if u not in to_visit:
                to_visit.add(u)
                todo = [u] + todo 
    print(counter[m])
