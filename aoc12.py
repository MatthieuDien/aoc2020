def rot(ori, angle):
    return Orientation((ori + angle //90) % 4)

with open("input-12-test", "r") as f:
    wx,wy = (10,1)
    x,y = (0,0)
    face = 1
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    for l in f:
        # print(x,wy,face)
        # print(l)
        instr, val = l[0], int(l[1:-1])
        if instr == "N":
            wx,wy = wx, wy+val
        elif instr == "S":
            wx,wy = wx, wy-val
        elif instr == "W":
            wx,wy = wx-val, wy
        elif instr == "E":
            wx,wy = wx+val, wy
        elif instr == "F":
            x,y = x+wx*val, y+wy*val
        elif instr == "L":
            face = (8 + face - val // 90) % 4
            if val // 90 % 4 == 1:
                wx, wy = -wy, wx
            elif val // 90 % 4 == 2:
                wx, wy = -wx, -wy
            elif val // 90 % 4 == 3:
                wx, wy = wy, -wx
            else:
                print(l)
                assert(False)
        elif instr == "R":
            face = (face + val // 90) % 4
            face = (8 + face - val // 90) % 4
            if val // 90 % 4 == 1:
                wx, wy = wy, -wx
            elif val // 90 % 4 == 2:
                wx, wy = -wx, -wy
            elif val // 90 % 4 == 3:
                wx, wy = -wy, wx
            else:
                print(l)
                assert(False)
        else :
            assert(False)
        if face < 0:
            print(l)
    print(x,y,wx,wy)
    print(sum(map(abs,(x,y))))
