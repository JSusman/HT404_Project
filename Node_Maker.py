import numpy as np
from matplotlib import pyplot as plt

class square:
    def __init__(self,side_len):
        self.side_len = side_len
    
    def area(side_len):
        area = side_len**2
        print(area)
        return area
    
    #This is how to get the number of node in the x and the y directions
    def node_spacing(side_len,delta_x,delta_y):
        x_spacing = side_len/delta_x
        y_spacing = side_len/delta_y
        print(round(x_spacing,0),round(y_spacing,0))
        return x_spacing,y_spacing
    
class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(width,length):
        area = width*length
        print(f"area of the pin is {area} mm")
        return area
    
    def plot_shape(width,length):
        plt.axes()
        rectangle = plt.Rectangle((0,0),width,length,ec='black')
        plt.gca().add_patch(rectangle)
        axis_x_up = width+3
        axis_x_low =-3#(width+3)*(-1)
        axis_y_up = length+3
        axis_y_low = 0
        plt.axis([axis_x_low,axis_x_up,axis_y_low,axis_y_up])
        plt.show()

    
    #In this instance width is the x-dir and length is y-dir
    #This is how to get the number of node in the x and the y directions
    def node_spacing(width,length,delta_x,delta_y,equal_delta,equal_delval):
        if equal_delta == True:
            x_spacing = equal_delval
            y_spacing = equal_delval
        else:    
            x_spacing = width/delta_x
            y_spacing = length/delta_y
        
        print(f'The node spacing in the x-direction is {round(x_spacing,0)}, the node spacing in the y-direction is {round(y_spacing,0)}')
        return x_spacing,y_spacing

class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(radius):
        area = np.pi*(radius**2)
        print(area)
        return area
    
    # def node_spacing():

# square.node_spacing(5,0.25,0.5)
rectangle.node_spacing(10,20,.5,.75,False,0)
rectangle.area(1,1)
rectangle.node_spacing(0,0,0,0,True,1)
rectangle.plot_shape(1,12.7)


# class Node:
#     def __init__(self,x,y):

# plt.show