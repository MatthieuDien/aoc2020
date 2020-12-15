from functools import reduce

def to_id(l):
    s = l[:-1]
    return int(s.translate(s.maketrans("BFRL","1010")),2)

with open("input-5","r") as f:
    # print(reduce(max,map(to_id, f),0))
    ids = set(map(to_id, f))
    m = max(ids)
    c = set(range(m)) - ids
    for x in c:
        if x-1 in ids and x+1 in ids:
            print(x)
