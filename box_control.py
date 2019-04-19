from random import randint
from func import *
import math
from smalldata import *
dtime=5
def init_boxs(box_numx,box_numy, win_width, win_height, life_num):
    # 初始化一个方块容器
    life_coordinate = get_life_coordinate(box_numx,box_numy,life_num)
    print(life_coordinate)
    boxs = []
    print("boxnumx",box_numx)
    print("boxnumy",box_numy)
    for x in range(0, box_numx):
        tmp = []
        for y in range(0, box_numy):
            if (x, y) in life_coordinate: #人的坐标
                print("gaga",x,y)
                value = 1
            else:
                value = M[x][y]  #其他坐标  yx互换
            tmp.append({
                'value': value,
                'x': x * (win_width / box_numx),
                'y': y * (win_height / box_numy),
                'width': win_width / box_numx,
                'height': win_height / box_numy
            })
        boxs.append(tmp)
    return boxs,life_coordinate

def get_life_coordinate(box_numx,box_numy, life_num):  #随机生成初始坐标
    ret = []
    
    for n in range(0, life_num):
        c = randint(0, 3)
        if c == 0 :
            #ret.append((randint(1, 80), randint(1, 7)))
            second=randint(2,15)
            first=randint(2,28)
            while((first,second) in ha.keys()):
                second=randint(2,15)
                first=randint(2,28)
            ha[(first,second)]=1
            ret.append((first,second))
        elif c == 1:
            second=randint(36,48)
            first=randint(2,28)
            while((first,second) in ha.keys()):
                second=randint(36,48)
                first=randint(2,28)
            ha[(first,second)]=1
            ret.append((first,second))
        elif c == 2:
            second=randint(2,25)
            first=randint(50,62)
            while((first,second) in ha.keys()):
                second=randint(2,25)
                first=randint(50,62)
            ha[(first,second)]=1
            ret.append((first,second))
        elif c ==3:
            second=randint(32,49)
            first=randint(50,62)
            while((first,second) in ha.keys()):
                second=randint(32,49)
                first=randint(50,62)
            ha[(first,second)]=1
            ret.append((first,second))
        """
        c = randint(0,3)
        if c == 0:
            ret.append((randint(280, 520), randint(50, 90)))
        elif c == 1:
            ret.append((randint(0, 280), randint(0,21)))
        elif c == 2:
            ret.append((randint(410,470), randint(200,270)))
        elif c == 3:
            ret.append((randint(653, 672), randint(59,215)))
        """

    return ret

def change_boxs(boxs,people,enter,f,delaytime):
    # 变换规则
        flag=-1
        for i in range(0,len(people)):
            for j in range(0,len(enter)):
                if (boxs[people[i].x][people[i].y]['value']==1 or boxs[people[i].x][people[i].y]['value']==11) and (abs(people[i].x-enter[j][0])==1 and abs(people[i].y-enter[j][1])==1) or (abs(people[i].x-enter[j][0])==0 and abs(people[i].y-enter[j][1])==1) or (abs(people[i].x-enter[j][0])==1 and abs(people[i].y-enter[j][1])==0):
                    boxs[people[i].x][people[i].y]['value']=0
                    if boxs[people[i].x][people[i].y]['value']==1:
                        flag=1
                    else:
                        flag=11                       
                # print("xiaochu",people[i].x,people[i].y)
                    people[i].stXY(-1,-1)
                    break
        for i in range(0,len(people)):
            if (boxs[people[i].x][people[i].y]['value']==1 or boxs[people[i].x][people[i].y]['value']==11) and people[i].x!=-1 and people[i].y!=-1:
                min = 10000
                if boxs[people[i].x][people[i].y]['value']==1:
                    flag=1
                    people[i].add()
                else:
                    flag=11
                    people[i].add()
                target = -1  # 标号为-1的入口
                for j in range(0, len(enter)):
                    view = create_view(people[i].x, people[i].y, enter[j][0], enter[j][1], M)
                    tempj = get_J(people[i].x, people[i].y, 1, 1, 1, enter[j][0], enter[j][1], view)
                    if tempj < min:
                        min = tempj
                        target = j
                nextX, nextY = direction(people[i].x, people[i].y, enter[target][0], enter[target][1], boxs, M)
                #print("next", nextX, nextY)
                if nextX == -1 and nextY == -1:
                    1
                else:
                    if (boxs[nextX][nextY]['value'] == 0):
                        if flag==1:
                            boxs[people[i].x][people[i].y]['value'] = 0
                            boxs[nextX][nextY]['value'] = 1
                            people[i].stXY(nextX, nextY)
                        else:
                            if delaytime>dtime:
                                boxs[people[i].x][people[i].y]['value'] = 0
                                boxs[nextX][nextY]['value']=11
                                people[i].stXY(nextX, nextY)                 
        if f:
            for i in range(0,len(people)):
                for j in range(0,len(enter)):
                    if (boxs[people[i].x][people[i].y]['value']==0.1) and (abs(people[i].x-enter[j][0])==1 and abs(people[i].y-enter[j][1])==1) or (abs(people[i].x-enter[j][0])==0 and abs(people[i].y-enter[j][1])==1) or (abs(people[i].x-enter[j][0])==1 and abs(people[i].y-enter[j][1])==0):
                        boxs[people[i].x][people[i].y]['value']=0
                        people[i].stXY(-1,-1)
                        break
            for i in range(0,len(people)):
                if boxs[people[i].x][people[i].y]['value']==0.1 and people[i].x!=-1 and people[i].y!=-1:
                    min = 10000
                    people[i].add()
                    target = -1  # 标号为-1的入口
                    for j in range(0, len(enter)):
                        view = create_view(people[i].x, people[i].y, enter[j][0], enter[j][1], M)
                        tempj = get_J(people[i].x, people[i].y, 1, 1, 1, enter[j][0], enter[j][1], view)
                        if tempj < min:
                            min = tempj
                            target = j
                    nextX, nextY = direction(people[i].x, people[i].y, enter[target][0], enter[target][1], boxs, M)
                    if nextX == -1 and nextY == -1:
                        1
                    else:
                        if (boxs[nextX][nextY]['value'] == 0):
                            boxs[people[i].x][people[i].y]['value'] = 0
                            boxs[nextX][nextY]['value'] = 0.1
                            people[i].stXY(nextX, nextY)
        
            


                
        






