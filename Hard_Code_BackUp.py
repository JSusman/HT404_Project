import numpy as np
import matplotlib.pyplot as plt
#HT Coeff - Convection
h1 = 100
h2 = 100
#Thermal Conductivy - Conduction
k = 2.5
#Temp. Surr - Tinfinity
Tinf = 20
#Temp at Base
Tbase = 75
#Node Spaceing
dx = .5
dy = .5
#Geometry
l = 15
w = 2
#Number of Total Nodes
node_num1 = 30
node_num2 = 4

T= np.zeros([node_num1,node_num2])

# T[(l-1):, :] = 0
# T[:1, :] = Tbase
# T[:, (w-1):] = Tinf
# T[:, :1] = Tinf

#Biot Number
Bi = round((h1*dx)/k,2)
c = 0
Bi_change = False 


for m in range(0,node_num1-1,1):    
    for n in range(0,node_num2-1,1):
       
       ##two h value options##
       if Bi_change == False:
        Bi = round((h1*dx)/k,2)
        Bi_change = not Bi_change
       else:
        Bi = round((h2*dx)/k,2)
        Bi_change = not Bi_change
       
       ##NODES##
       ################################################################################# 
       ##SPECIAL CASES##
       if c <= 2:#Base
        T[m][n] = 75
        c+=1
       elif 2<c<=3:#Left
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+75)+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1    
       elif 3<c<=4:#Center
        T[m][n]= round((T[m][n+1]+75+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif 4<c<=5:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+75)+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       ##END OF SPECIAL CASES##
       ################################################################################# 
       
       elif c==6:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==7:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==8:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==9:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==10:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==11:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==12:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==13:#Center
         T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
         c+=1
       elif c==14:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==15:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==16:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==17:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==18:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==19:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==20:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==21:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==22:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==23:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==24:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==25:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==26:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==27:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==28:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==29:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==30:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==31:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==32:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==33:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==34:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==35:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==36:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==37:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==38:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==39:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==40:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==41:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1 
       elif c==42:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==43:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==44:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==45:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==46:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==47:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==48:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==49:#Center
         T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
         c+=1
       elif c==50:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==51:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==52:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==53:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==54:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==55:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==56:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==57:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==58:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==59:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==60:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==61:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==62:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==63:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==64:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==65:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==66:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==67:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==68:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==69:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==70:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==71:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==72:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==73:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==74:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==75:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==76:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==77:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1 
       elif c==78:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==79:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==80:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==81:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==82:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==83:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==84:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==85:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==86:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==87:#Left 
        T[m][n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1
       elif c==88:#Center
        T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
        c+=1
       elif c==89:#Right
        T[m][n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
        c+=1

    
    
    
    
    
    #    elif c==87:#Left 
    #     T[m,n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==88:#Center
    #     T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
    #     c+=1
    #    elif c==89:#Right
    #     T[m,n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==90:#Left 
    #     T[m,n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==91:#Center
    #     T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
    #     c+=1
    #    elif c==92:#Right
    #     T[m,n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==93:#Left 
    #     T[m,n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==94:#Center
    #     T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
    #     c+=1
    #    elif c==95:#Right
    #     T[m,n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==96:#Left 
    #     T[m,n] = round((((2*T[m+1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1
    #    elif c==97:#Center
    #     T[m][n]= round((T[m][n+1]+T[m][n-1]+T[m+1][n]+T[m-1][n])/4,2)
    #     c+=1
    #    elif c==98:#Right
    #     T[m,n] = round((((2*T[m-1][n])+T[m][n+1]+T[m][n-1])+(2*(Bi)*Tinf))/(2*(Bi+2)),2)
    #     c+=1 
    #    else:
    #     T[m][n] = 0
    #     c+=1

with open('Temp.txt', 'w') as testfile:
    for row in T:
        testfile.write(' '.join([str(a) for a in row]) + '\n')

