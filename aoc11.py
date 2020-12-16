with open("input-11", "r") as f:
    w,h = 0,0
    seats = ""
    for l in f:
        seats += "L"+l[:-1]+"L"
        h += 1
        w = len(l)-1
    seats = "L"*(w+2) + seats + "L"*(w+2)
    print("toto", w,h)

# def neighbors(seats,i,j):
#     # print(i,j)
#     l = ""
#     for a in range(i-1,i+2):
#         for b in range(j-1, j+2):
#             if a != i or b != j:
#                 # print(a,b,a*(w+2) + b, len(seats)) # 
#                 l += seats[a*(w+2) + b]
#     # print(l)
#     return l

def neighbors(seats,i,j):
    # print(i,j)
    l = ""
    for p in range(-1,2):
        for q in range(-1,2):
            # print(p,q)
            if not( p == 0 and q == 0):
                a, b = i+p, j+q
                while seats[a*(w+2) + b] == ".":
                    a, b = a+p, b+q
                l += seats[a*(w+2) + b]
    # print(i,j,l)
    return l

def transition(seats):
    new_seats = "L"*(w+2)
    # print(w,h,seats)
    for j in range(1,h+1):
        new_seats += "L"
        for i in range(1,w+1):
            k = neighbors(seats,j,i).count("#")
            # print(k)
            if k == 0 and seats[j*(w+2)+i] == "L":
                new_seats += "#"
            elif k >= 5 and seats[j*(w+2)+i] == "#":
                new_seats += "L"
            else:
                new_seats += seats[j*(w+2)+i]
        new_seats += "L"
    new_seats += "L"*(w+2)
    return new_seats

old_seats = ""
c = 0
   
while old_seats != seats:
    for j in range(1,h+1):
        print(seats[(1+j*(w+2)):(j*(w+2)+w+1)])

    print("")
    old_seats, seats = seats, transition(seats)
    c += 1
print(c)
for j in range(1,h+1):
    print(seats[(j*(w+2)):(j*(w+2)+w+2)])
print(seats)
print(seats.count("#"))
        
    
