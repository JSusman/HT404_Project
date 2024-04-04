import numpy as np
import matplotlib.pyplot as plt

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

# Define the vertices of the custom shape (a triangle in this case)
vertices = np.array([[0, 0], [4, 0], [4,11.5], [7,11.5], [7,12.5], [3,12.5], [3,1], [0,1]])

spacing = 0.5

# # Initialize an empty list to store all points
# all_points = []

# # Ensure vertices are ordered correctly
# vertices = np.array(sorted(vertices, key=lambda x: x[0]))

# # Loop through each pair of consecutive vertices
# for i in range(len(vertices)):
#     # Get the current vertex and the next vertex (with wrap-around for the last vertex)
#     current_vertex = vertices[i]
#     next_vertex = vertices[(i + 1) % len(vertices)]
    
#     # Calculate the slope and intercept for the line between the current and next vertex
#     slope = (next_vertex[1] - current_vertex[1]) / (next_vertex[0] - current_vertex[0])
#     intercept = current_vertex[1] - slope * current_vertex[0]
    
#     # Calculate the number of samples, ensuring it's non-negative
#     num_samples = int((next_vertex[0] - current_vertex[0]) / spacing)
#     if num_samples < 0:
#         # If the difference is negative, reverse the order of vertices for this iteration
#         current_vertex, next_vertex = next_vertex, current_vertex
#         slope = (next_vertex[1] - current_vertex[1]) / (next_vertex[0] - current_vertex[0])
#         intercept = current_vertex[1] - slope * current_vertex[0]
#         num_samples = int((next_vertex[0] - current_vertex[0]) / spacing)
    
#     # Generate points along the line between the current and next vertex
#     x_values = np.linspace(current_vertex[0], next_vertex[0], num_samples)
#     y_values = slope * x_values + intercept
    
#     # Append the generated points to the list
#     all_points.extend(list(zip(x_values, y_values)))

# # Convert the list of points to a NumPy array
# all_points = np.array(all_points)

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Add the polygon to the plot
# ax.add_patch(plt.Polygon(vertices, fill=None, edgecolor='r'))

# # Plot the points
# ax.scatter(all_points[:, 0], all_points[:, 1], color='blue', s=10, alpha=0.5)

# # Set the limits of the plot to ensure the grid covers the entire shape
# ax.set_xlim(np.min(vertices[:, 0]) - 1, np.max(vertices[:, 0]) + 1)
# ax.set_ylim(np.min(vertices[:, 1]) - 1, np.max(vertices[:, 1]) + 1)

# # Overlay a grid
# ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# # Display the plot
# plt.show()


# Create a Polygon object
polygon = plt.Polygon(vertices, fill=None, edgecolor='r')

# Create a figure and axis
fig, ax = plt.subplots()

# Add the polygon to the plot
ax.add_patch(polygon)

# Set the limits of the plot to ensure the grid covers the entire shape
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 13)

# Overlay a grid
ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# Define the spacing for x and y axes
spacing = 0.5

# Set the ticks on both axes with the defined spacing
ax.set_xticks(np.arange(-1, 13, spacing)) # Adjust the range as needed
ax.set_yticks(np.arange(-1, 13, spacing)) # Adjust the range as needed

x_points = np.arange(-1, 13, spacing)
y_points = np.arange(-1, 13, spacing)
x_grid, y_grid = np.meshgrid(x_points, y_points)

# Flatten the grid points to use with scatter
points = np.vstack([x_grid.ravel(), y_grid.ravel()]).T



# Filter points to only those that lie on the shape's edges
# This is a simplified example. For more complex shapes, you might need a more sophisticated approach.
filtered_points = []
for point in points:
    if polygon.contains_point(point):
        filtered_points.append(point)

# Convert filtered_points to a NumPy array
filtered_points = np.array(filtered_points).reshape(-1, 2)
print(filtered_points)

# Now you can index it correctly
ax.scatter(points[:, 0], points[:, 1], color='blue', s=10, alpha=0.5)

# Display the plot
plt.show()