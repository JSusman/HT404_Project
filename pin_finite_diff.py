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


w = 1
l = 12.7
node_spacing = .25
outer_nodes = l/node_spacing
top_nodes = w/node_spacing

print(outer_nodes,top_nodes)