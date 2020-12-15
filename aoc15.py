l = [1,0,15,2,10,13]
# l = [0,3,6]


last_seen = {x : i+1 for i,x in enumerate(l[:-1])}

for i in range(len(l),30000000):
    # print(last_seen)
    # print(l)
    if l[-1] not in last_seen:
        last_seen[l[-1]] = i
        l.append(0)
    else:
        old = last_seen[l[-1]]
        last_seen[l[-1]] = i
        x = i-old
        # print(l[-1],old,i)
        l.append(x)
print(l[-1])
    
