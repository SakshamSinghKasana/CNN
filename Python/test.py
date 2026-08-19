import numpy as np 

D1 = [
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
        ]

D = [
        [1,1,1,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0]
        ]
fil = [
        [1,0,-1],
        [1,0,-1],
        [1,0,-1]
        ]

def cal(sm, fil, r):
    sm1 = sm.tolist()
    sum = 0
    for i in range(r):
        for j in range(r):
            m = sm1[i][j]*fil[i][j]
            sum+=m 
    return sum

d = np.array(D)

activation_M = []
stride = 1
filt = 3
Yl = 0
for a in range(filt,len(d)+1):
    Xl=0
    row = []
    for b in range(filt,len(d)+1):
        sm = d[Yl:a, Xl:b] #The matrix that is scanned by the filter

        #____________Write the filter calculation here_____________
        row.append(cal(sm,fil, filt))


        Xl+=stride
    # print(sm)
    Yl+=stride
    activation_M.append(row)

print(activation_M)
