from functools import reduce

def is_valid(l):
    l = map(lambda x : x[:-1].split(" "), l)
    s = reduce(lambda a,b:dict(a, **b),
               map(lambda ll: dict(map(lambda x: x.split(":"), ll)), l),
               dict())
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(set(s.keys())):
        try:
            return ((1920 <= int(s["byr"]) <= 2002) and
                    (2010 <= int(s["iyr"]) <= 2020) and
                    (2020 <= int(s["eyr"]) <= 2030) and
                    ((s["hgt"][-2:] == "cm" and 150 <= int(s["hgt"][:-2]) <= 193)
                     or (s["hgt"][-2:] == "in" and 59 <= int(s["hgt"][:-2]) <= 76)) and
                    (s["hcl"][0] == "#" and len(s["hcl"]) == 7 and int(s["hcl"][1:], 16)) and
                    (s["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) and
                    (len(s["pid"]) == 9 and int(s["pid"])))
        except:
            return False
        else:
            return False
        
with open("input-4","r") as f:
    passport = []
    nb_valid = 0
    for l in f:
        if l == "\n":
            nb_valid += bool(is_valid(passport))
            passport = []
        else:
            passport.append(l)
    nb_valid += bool(is_valid(passport))
    print(nb_valid)
