from collections import defaultdict, Counter

with open("input-7", "r") as fd:
    dico = Counter()
    dico2 = defaultdict(lambda : set())
    for line in fd:
        l = line.split(" ")
        bag = l[0] + " " + l[1]
        dico[bag] = Counter()
        for i in range(4,len(l),4):
            if l[i] != "no":
                b = l[i+1] + " " + l[i+2]
                dico[bag] += Counter({b:int(l[i])})
                dico2[b].add(bag)

# Part 1
to_visit = ["shiny gold"]
visited = set()
while to_visit:
    b = to_visit.pop()
    visited.add(b)
    for bag in dico2[b]:
        if bag not in visited:
            to_visit.append(bag)
print(len(visited)-1)

# Part2
to_visit = Counter({"shiny gold":1})
count = Counter()
while to_visit:
    bag,n = to_visit.popitem()
    count += Counter({bag:n})
    for b in dico[bag]:
        to_visit += Counter({b:dico[bag][b]*n})
print(sum(count.values())-1)
    
