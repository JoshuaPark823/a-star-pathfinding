from tkinter import *

# Define the Node() class
class Node():

    # Set the default constructor of each node
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        # The default g_cost and h_cost values are going to be set to 0
        self.g_cost = 0
        self.h_cost = 0


# Create the main window object and set some parameters
window = Tk()
window.title("A* Visualization")
window.geometry("900x675")

"""

A* Pathfinding Implementation:

1. Create a Node class that defines each node
    - Note: Not all of the grid squares are nodes. Nodes have a parent and a grid position and are only created
    when they need to be.

2. Create the grid constant and have it displayed
    - The grid is going to be a 2D matrix with x and y representing grid positions.
    - Display the grid as squares in the main window.
        - g_cost in top left, h_cost in top right, f_cost in the center
        - current_node

3. 


"""
# Open up the main window :)
window.mainloop()
