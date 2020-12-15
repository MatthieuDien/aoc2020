
with open("input-6","r") as f:
    answer = set()
    restart = True
    n = 0
    for l in f:
        if l == "\n":
            n += len(answer)
            answer = set()
            restart = True
        elif restart:
            answer = set(l[:-1])
            restart = False
        else:
            answer &= set(l[:-1])
    n += len(answer)
    print(n)


from functools import reduce

with open("input-6") as f:
    gs = f.read().split("\n\n")
    print(sum(map(lambda g: len(set(g.replace("\n",""))), gs)))
    print(sum(map(lambda g: len(reduce(lambda x, y: x & y, map(set, g.splitlines()))), gs)))
