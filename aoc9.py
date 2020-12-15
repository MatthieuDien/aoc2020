from itertools import combinations

with open("input-9","r") as f:
    l = list(map(lambda x: int(x[:-1]), f))


part1 = None
for i in range(25, len(l)):
    s = set(map(sum,combinations(l[i-25:i],2)))
    if l[i] not in s:
        part1 = (i, l[i])
        break


for i in range(part1[0]):
    for j in range(i+1,part1[0]):
        if sum(l[i:j]) == part1[1]:
            print(min(l[i:j]) + max(l[i:j]))
            break
