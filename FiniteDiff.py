
class Node:
    
    def __init__(self,case):#(self,Case1,Case2,Case3,Case4,Case5,hkdeltax):
        self.case = case
        return case
        # self.Case1 = Case1
        # self.Case2 = Case2
        # self.Case3 = Case3
        # self.Case4 = Case4
        # self.Case5 = Case5
        # self.hkdeltax = hkdeltax

    def hkdeltax(h,k,deltax):
     caseCons = (h*deltax)/k
     return caseCons

    #Case 1: Interior Node
    def Case1(Txplus,Txminus,Typlus,Tyminus,T_inital,nodes):
     Case1_Tmn=(Typlus + Tyminus + Txplus + Txminus)/4
     


     return Case1_Tmn

    #Case 2: Node at an internal corner with Convection
    def Case2(Txplus,Txminus,Typlus,Tyminus,Tinf,caseCons):
     Case2_Tmn = (2(Txminus+Typlus)+(Txplus+Tyminus)+2*caseCons*Tinf)/(2*(3+caseCons))
     return Case2_Tmn

    #Case 3: Node at a plane surface with C0onvection
    def Case3(Txplus,Txminus,Typlus,Tyminus,Tinf,caseCons):
        Case3_Tmn = ((Txminus+Typlus+Tyminus)+2*caseCons*Tinf)/2*(caseCons+2)
        return Case3_Tmn

    #Case 4: Node at an external corner with convection
    def Case4(Txplus,Txminus,Typlus,Tyminus,Tinf,caseCons):
        Case4_Tmn = ((Tyminus+Txminus) + 2*caseCons*Tinf)/(2*(caseCons+1)) 
        return Case4_Tmn

    #Case 5: Node at a plane surface with uniform heat flux
    def Case5(Txplus,Txminus,Typlus,Tyminus,Tinf,caseCons,htflx,dx,k):
        Case5_Tmn = ((2*Txminus+Typlus+Tyminus)+((2*htflx*dx)/k))/4
        return Case5_Tmn

class Pin:

    def __init__(self,Node):
       self.Node = Node

    

width = 1
length = 12.7 
node_spacing = 0.25


n_case2 = length/node_spacing
n_case3 = width + length*2/node_spacing

print(n_case2,n_case3)
      
