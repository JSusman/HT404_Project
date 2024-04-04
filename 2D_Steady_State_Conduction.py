import numpy as np
import matplotlib.pyplot as plt

#HT Coeff - Convection
h = 100
#Thermal Conductivy - Conduction
k = 2.5
#Heat Flux
q2 = 5
#Temp. Surr - Tinfinity
Tinf = 20
#Node Spaceing
dx = .5
dy =.5
#Geometry
l = 14.5
w = 1
#Number of Total Nodes
node_num = int((((l)/.5)*3))


list = []
for i in range(1,node_num+1):
    list.append(i)

T = np.zeros([len(list),len(list)])

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

is_left = True
is_not_left = False

counter = 0 
for m,n in zip(range(len(list)),range(len(list))):
    #for n in range(0,node_num-1):
        print(T)
        counter +=1

        # if m == 0: # At the start
        #  is_left = True
        #  is_not_left = False
        # elif m == len(list) - 1: # At the end
        #  is_left = False
        #  is_not_left = True

        # if is_left and is_not_left:
        # # This condition will never be true due to the initialization and the logic above
        #  pass

        # if is_left == False and is_not_left == True:
        #  #CASE 3 Right : T[m-1,n]
        #  T[m,n] = ( ((2 * T[m-1,n]) + T[m,n+1] + T[m,n-1] ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
        #  is_left == True
        #  is_not_left == False
        #  print(f"I am node {m} at {T[m,n]} degrees, on the right side") 

        # if is_left == True and is_not_left == False:
        #  #CASE 3 Left : T[m+1,n]
        #  T[m,n] = ( ((2 * T[m+1,n]) + T[m,n+1] + T[m,n-1] ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
        #  is_left = False
        #  is_not_left = True
        #  print(f"I am node {m} at {T[m,n]} degrees, on the left side")  
        
        case_3T = m,n
        print(case_3T)
        ## Bottom 3 Nodes are 75 degrees ##
        if m == 1:
           T = 75
        elif counter == 2:
           T = 75
        elif counter == 3:
           T = 75
        ################################### 
        

        ## Nodes 4(case 3),5(case 1),6(case 3) need Temp. set to 75 as well ##        
        elif counter == 4:
           #CASE 3 Left: T[m+1,n]
           T[m,n] = ( ((2 * T[m+1,n]) + T[m,n+1] + 75 ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
        elif counter == 5:
           #CASE 1
           T[m,n]= ( T[m,n+1] + 75 + T[m+1,n] + T[m-1,n] ) / 4
        elif counter == 6:
           #CASE 3 Right : T[m-1,n]
           T[m,n] = ( ((2 * T[m-1,n]) + T[m,n+1] + 75 ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
        ######################################################################
print(len(T))
print(counter)


## SCRAP PILE ##
 #CASE 1
 #T[m,n]= ( T[m,n+1] + T[m,n-1] + T[m+1,n] + T[m-1,n] ) / 4 
 #print(f'case 1 {T[m,n]}')
 #CASE 2
 #T[m,n] = ( 2 * (T[m-1,n] + T[m,n+1] ) + ( T[m+1,n] + T[m,n-1] ) + 2 * (conCons) * Tinf )/ (2 * ( 3 + conCons ) )
 #CASE 3
 #T[m,n] = ( ((2 * T[m-1,n]) + T[m,n+1] + T[m,n-1] ) + (2 * (conCons) * Tinf ) )/ (2 * ( conCons + 2 ) )
 #CASE 4
 #T[m,n] = ( ( T[m,n-1]) + T[m-1,n]) + (2 * (conCons) * Tinf ) / (2 * ( conCons + 1 ) )
 #CASE 5
 #T[m,n] = ( 2 * T[m-1,n] + T[m,n+1] + T[m,n-1] + C5_Cons) / 4
 #T[m-1,n] = ( 2 * C5_Cons - 4 * T[m,n] ) / ( 2 + T[m,n+1] + T[m,n-1] )


##This was just a way to visualize the nodes on the shape##
# # Define the vertices
# vertices = np.array([[0, 0], [4, 0], [4,11.5], [7,11.5], [7,12.5], [3,12.5], [3,1], [0,1]])

# spacing = 0.5

# # Create a Polygon object
# polygon = plt.Polygon(vertices, fill=None, edgecolor='r')

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Add the polygon to the plot
# ax.add_patch(polygon)

# # Set the limits of the plot to ensure the grid covers the entire shape
# ax.set_xlim(-1, 8)
# ax.set_ylim(-1, 13)

# # Overlay a grid
# ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# # Define the spacing for x and y axes
# spacing = 0.5

# # Set the ticks on both axes with the defined spacing
# ax.set_xticks(np.arange(-1, 13, spacing)) # Adjust the range as needed
# ax.set_yticks(np.arange(-1, 13, spacing)) # Adjust the range as needed

# x_points = np.arange(-1, 13, spacing)
# y_points = np.arange(-1, 13, spacing)
# x_grid, y_grid = np.meshgrid(x_points, y_points)

# # Flatten the grid points to use with scatter
# points = np.vstack([x_grid.ravel(), y_grid.ravel()]).T



# # Filter points to only those that lie on the shape's edges
# # This is a simplified example. For more complex shapes, you might need a more sophisticated approach.
# filtered_points = []
# for point in points:
#     if polygon.contains_point(point):
#         filtered_points.append(point)

# # Convert filtered_points to a NumPy array
# filtered_points = np.array(filtered_points).reshape(-1, 2)
# print(filtered_points)

# # Now you can index it correctly
# ax.scatter(points[:, 0], points[:, 1], color='blue', s=10, alpha=0.5)

# # Display the plot
# plt.show()