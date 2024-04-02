import numpy as np
#HT Coeff - Convection
h = 100
#Thermal Conductivy - Conduction
k = 2.5
#Heat Flux
q2 = 5
#Temp. Surr - Tinfinity
Tinf = 75
#Node Spaceing
dx = .5
dy =.5
#Number of Total Nodes
node_num = 10


T = np.zeros((node_num,node_num))

def condCons(h,k,dx):
     cCons = round((h*dx)/k,2)
     return cCons

def hFluxCons(q2,dx,k):
    hFCons = (2*q2*dx)/k 
    return hFCons

conCons = condCons(h,k,dx)
C5_Cons = hFluxCons(q2,dx,k)

#special nodes at 1,6,22,29,30,31,36,58,66,
#node_num = 105

for m in range(1,node_num-1):
    for n in range(1,node_num-1):
        
        if n == 5:
            #CASE 1
            T[m,n]= ( T[m,n+1] + T[m,n-1] + T[m+1,n] + T[m-1,n] ) / 4 
            print(f'case 1 {T[m,n]}')
        
        elif n == 4:
           #CASE 2
           T[m,n] = ( 2 * (T[m-1,n] + T[m,n+1] ) + ( T[m+1,n] + T[m,n-1] ) + 2 * (conCons) * Tinf )/ (2 * ( 3 + conCons ) )

        elif n == 3:
           #CASE 3
           T[m,n] = ( ((2 * T[m-1,n]) + T[m,n+1] + T[m,n-1] ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
    
        elif n == 2:
           #CASE 4
           T[m,n] = ( ( T[m,n-1]) + T[m-1,n]) + (2 * (conCons) * Tinf ) / (2 * ( conCons + 1 ) )

        elif n == 1:
            #For this case the temperature is the same as the server T[m,n] = base temperature#
            T[m,n+1] = 1
            T[m,n-1] = 1
            T[m,n] = 75
            #CASE 5
            #T[m,n] = ( 2 * T[m-1,n] + T[m,n+1] + T[m,n-1] + C5_Cons) / 4
            T[m-1,n] = ( 2 * C5_Cons - 4 * T[m,n] ) / ( 2 + T[m,n+1] + T[m,n-1] )
            print(f'case 5 {T[m-1,n]}')#print(f'case 5 {T[m,n]}')
        
        
