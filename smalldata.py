M = []
enter = []
x = 64
y = 51
ha={}
for i in range(0,y):
    tmp = [0] * x
    M.append(tmp)

#i竖直 j 横向
for i in range(0,64): #横
    M[0][i] = -1
    M[50][i] = -1
    ha[(0,i)]=1
    ha[(50,i)]=1

for j in range(0,51): #纵
    M[j][0] = -1
    M[j][63] = -1
    ha[(j,0)]=1
    ha[(j,63)]=1
for i in range(10,15): #横
    M[20][i] = -1
    M[35][i] = -1
    ha[(20,i)]=1
    ha[(35,i)]=1

for j in range(20,36):  #纵
    M[j][10] = -1
    M[j][15] = -1
    ha[(j,10)]=1
    ha[(j,15)]=1
for j in range(0,51):  #纵
    M[j][30] = -1
    M[j][48] = -1
    ha[(j,30)]=1
    ha[(j,48)]=1

for i in range(48,63): #横
    M[30][i] = -1
    ha[(30,i)]=1

for i in range(30,36): #横
    M[12][i] = -1
    ha[(12,i)]=1
for j in range(0,13):  #纵
    M[j][36] = -1
    ha[(j,36)]=1
"""door"""
for j in range(28,35):  #纵
    M[j][30] = 0
for j in range(20,23):  #纵
    M[j][48] = 0
    M[j+20][48] = 0
for i in range(32,34): #横
    M[12][i] = 0

"""exit"""
for i in range(40,42): #横
    M[0][i] = 2
    enter.append((i,0))
for i in range(32,36): #横
    M[50][i] = 2
    enter.append((i, 50))

"""随机范围
for i in range(2,15):
    for j in range(2,28):
        M[i][j] = 3
for i in range(36,48):
    for j in range(2,28):
        M[i][j] = 3
for i in range(2,25):
    for j in range(50,62):
        M[i][j] = 3
for i in range(32,49):
    for j in range(50,62):
        M[i][j] = 3
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