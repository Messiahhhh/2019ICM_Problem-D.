M = []
enter = []
x = 668+3+3
y = 268+3+3 #3为边框线宽度
"""
for i in range(0,y):
    tmp = [0] * x
    M.append(tmp)

"""
for i in range(0,y):
    tmp = [0] * x
    M.append(tmp)

#i竖直 j 横向
for i in range(0,21): #左边线
    for j in range(0, 3):
        M[i][j] = -1
        M [y-i-1][j] = -1

for i in range(0,3): #上下边线
    for j in range(0, 480):
        M[i][j] = -1
        M [y-i-1][j] = -1

for i in range(18+3,18+3+3): #上下内边线 左
    for j in range(0, 280):
        M[i][j] = -1
        M [y-i-1][j] = -1

for i in range(18+3+3+63,18+3+3+63+3): #上下方块 横
    for j in range(280, 520):
        M[i][j] = -1
        M [y-i-1][j] = -1

for i in range(18+3,18+3+3+63+3): #上下方块 纵
    for j in range(278, 281):
        M[i][j] = -1
        M [y-i-1][j] = -1


for i in range(56+3,y - 56 -3): #右边线
    for j in range(x-3,x):
        M[i][j] = -1

for i in range(56+3,56+3+3): #右方块 横
    for j in range(x-188-3,x):
        M[i][j] = -1
        M[y-i-1][j] = -1

for i in range(0,56+3+3): #右方块 短纵
    for j in range(480,480+3):
        M[i][j] = -1
        M[y-i-1][j] = -1 #上下对称

for i in range(87,87+100): #右方块 左纵
    for j in range(520,520+3):
        M[i][j] = -1


for i in range(62+18,62+145+3-18): #右方块 内矩形纵
    for j in range(x-18-3,x-18):
        M[i][j] = -1
        M[i][j - 114] = -1

for i in range(62+18,62+18+3): #右方块 内矩形横
    for j in range(x-18-3-114,x-18):
        M[i][j] = -1
        M[y - i - 1][j] = -1  # 上下对称


"""下方块的内部 """

for i in range(200,200+54):
    for j in range(340,340+3): #纵
        M[i][j] = -1
        M[i][j - 40] = -1 #左块
        M[i][j+58] = -1
        M[i][j+18] = -1  # 右块

for i in range(200,200+3):
    for j in range(300,300+40): #横
        M[i][j] = -1
        M[180 - i - 1][j] = -1
        M[i][j+58] = -1
        M[180 - i - 1][j+58] = -1
"""
for i in range(200,270):
    for j in range(410,470):
        M[i][j] = 0.1
"""


"""添加门"""

for j in range(300, 320):  #上下边线
    for i in range(0, 3):
        M[i][j] = 2
    enter.append((i, j))
"""
for j in range(300, 320):  # 上下边线
    for i in range(0, 3):
        M[y - i - 1][j] = 2
    enter.append((y - i - 1, j))
"""


"""转置 """
T = []
for i in range(0,x):
    tmp = [0] * y
    T.append(tmp)
for i in range(0,x):
    for j in range(0,y):
        T[i][j] = M [j][i]

M = T