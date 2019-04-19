import math

def create_view(x, y, enter_x, enter_y, M):#x=0,y=2. enter_x=0,enter_y=2,M
    view = []
    if x == enter_x or y == enter_y:
        if x == enter_x:
            if y - enter_y > 0:
                view.append(M[x][enter_y:y]);  # 修改
            else:
                view.append(M[x][y:enter_y]);  # 修改
        else:
            for i in range(enter_x, x):
                if y - enter_y > 0:
                    view.append([M[x][y]]);  # 修改
                else:
                    view.append([M[x][y]]);  # 修改
    else:
        if x - enter_x > 0:
            for i in range(enter_x, x):
                if y - enter_y > 0:
                    view.append(M[i][enter_y:y]);  # 修改
                else:
                    view.append(M[i][y:enter_y]);  # 修改
        else:
            for i in range(enter_x, x):
                if y - enter_y > 0:
                    view.append(M[i][enter_y:y]);  # 修改
                else:
                    view.append(M[i][y:enter_y]);  # 修改
    return view

def get_D(x,y,enter_x, enter_y):
    return math.sqrt((x - enter_x) ** 2 + (y - enter_y) ** 2)

def get_P(view):
    p = 0
    for i in view:
        for j in i:
            if j == 1:
                p += 1
    return p

def get_O(view):
    o = 0
    for i in view:
        for j in i:
            if j == 2:
                o += 1
    return o

def get_rP(view):
    p = get_P(view)
    N = 0
    for i in view:
        N += len(i)
    S = 0.6 * 0.6
    return p / (N * S)

def get_rO(view):
    o = get_O(view)
    N = 0
    for i in view:
        N += len(i)
    S = 0.6 * 0.6
    return o / (N * S)

def get_J(x,y,alph1, alph2, alph3, enter_x, enter_y, view):
    d = get_D(x,y,enter_x, enter_y)
    p = get_P(view)
    o = get_O(view)
    j = alph1 * d + alph2 * p + alph3 * o
    return j

def direction(x,y,xe, ye,boxs,M):#x=1,y=2,xe=0,ye=2
    J = [1111]*4
    if x == xe:  # 与出口同轴
        if ye > y:
            lx = [x-1, x, x+1]  # lx=0,1,2
            ly = [y+1, y+1, y+1]  # ly=2,2,2
        else:
            lx = [x - 1, x, x + 1]
            ly = [y - 1, y - 1, y - 1]
        count = 0
        for k in range(0, 3):
            if boxs[lx[k]][ly[k]]['value'] == 0:
                v = create_view(lx[k], ly[k], xe, ye, M)
               # print("xtong",v)
                J[k] = get_J(x, y, 1, 1, 1, xe, ye, v)
                #print("J", J)
            else:
                count += 1
                continue
        if count == 3:
            return -1,-1
        min = 100000
        mark = -1
        for i in range(0, 3):
            if J[i] < min:
                min = J[i]
                mark = i

    elif  y == ye:
       # print("ofg")
        if xe > x:
            lx = [x+1, x+1, x+1]  # lx=0,1,2
            ly = [y-1, y, y+1]  # ly=2,2,2
        else:
            lx = [x-1, x-1, x-1]
            ly = [y-1, y, y+1]
        count = 0
        for k in range(0, 3):
            if boxs[lx[k]][ly[k]]['value'] == 0:
                v = create_view(lx[k], ly[k], xe, ye,M)#xe=0,ye=2||0,2.1,2.2,2
               # print("ytong", v)
                J[k] =  get_J(x,y,1, 1, 1, xe, ye, v)
                #print("JJ",J)
            else:
                count += 1
                continue
        if count == 3:
            return -1,-1
        min = 100000
        mark = -1
        for i in range(0, 3):
            if J[i] < min:
                min = J[i]
                mark = i
    else:  # 与出口不同轴
        if xe >  x and ye >  y:
            lx = [ x,  x + 1,  x + 1]
            ly = [ y + 1,  y + 1,  y]
        elif xe >  x and ye <  y:
            lx = [ x + 1,  x + 1,  x]
            ly = [ y,  y - 1,  y - 1]
        elif xe < x and ye > y:
            lx = [x, x - 1, x - 1]
            ly = [y + 1, y + 1, y]
        else:
            lx = [ x,  x - 1,  x - 1]
            ly = [ y - 1,  y - 1,  y]
        count = 0
        for k in range(0, 3):
            if boxs[lx[k]][ly[k]]['value'] == 0:
                v = create_view(lx[k], ly[k], xe, ye,M)
                #print("butong", v)
                J[k] = get_J(x, y, 1, 1, 1, xe, ye, v)
               # print("JJJ",J)
            else:
                count += 1
                continue
        if count == 3:
            return -1,-1
        min = 100000
        mark = -1
        for i in range(0, 3):
            if J[i] < min:
                min = J[i]
                mark = i
    #print(mark)
    return  lx[mark],ly[mark]
