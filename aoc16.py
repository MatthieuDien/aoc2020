with open("input-16","r") as f:
    lines = f.readlines()
    i = 0
    constraints = []
    while lines[i] != "\n":
        ranges = lines[i][:-1].split(": ")[1].split(" or ")
        for r in ranges:
            r1, r2 = map(int, r.split("-"))
            constraints.append(set(range(r1,r2+1)))
        i+=1
    i += 5
    r = 0
    valid_tickets = []
    while i < len(lines):
        ticket = map(int,lines[i][:-1].split(","))
        valid = True
        for v in ticket:
            if all(map(lambda c: v not in c, constraints)):
                r += v
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)
        i+=1
    # Part 1
    print(r)
            
