def parse_eq(l):
    res = [lambda x : x]
    print(l)
    for c in l:
        print(res)
        if c in set(map(str,range(10))):
            res[-1] = res[-1](int(c))
        elif c == "+":
            res[-1] = lambda x : res[-1] + x
        elif c == "*":
            res[-1] = lambda x : res[-1] * x
        elif c == "(":
            res.append(lambda x : x)
        elif c == ")":
            res[-2] = res[-2](res[-1])
            del res[-1]
        else:
            pass
    return res[-1]
            
with open("input-18","r") as f:
    print(sum(map(lambda l: parse_eq(l[:-1]), f)))
        
