def set_bit(n, i, v):
    return n & ~(1<<i) | (v<<i)

def apply_mask(val, mask):
    m = 0
    n = val
    
    for i,v in enumerate(mask[::-1]):
        if v != "X" and v != "0":
        #    n = set_bit(n,i,int(v))
            n = set_bit(n,i,1)
                
    # print(bin(n))
    ns = []
    for i,v in enumerate(mask[::-1]):
        # print(" ns : ", ns)
        if v == "X":
            if len(ns) == 0:
                ns.append(set_bit(n,i,0))
                ns.append(set_bit(n,i,1))
            else:
                new_ns = []
                for n in ns:
                    new_ns.append(set_bit(n,i,0))
                    new_ns.append(set_bit(n,i,1))
                ns = new_ns
    # for n in ns:
    #     print(n,bin(n))
    return ns


with open("input-14", "r") as f:
    mask = None
    mem = dict()
    for line in f:
        if line[:4] == "mask":
            mask = line[:-1].split(" = ")[1]
        else:
            case, val = line[:-1].split(" = ")
            case = int(case[4:-1])
            val = int(val)
            # mem[case] = apply_mask(val, mask)
            for c in apply_mask(case, mask):
                mem[c] = val
    print(sum(mem.values()))
