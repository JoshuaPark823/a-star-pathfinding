from tkinter import *
import copy

"""
    A* Pathfinding Implementation:

    1. Create a Node class that defines each node
        - Note: Not all of the grid squares are nodes. Nodes have a parent and a grid position and are only created
        when they need to be.

    2. Create the start node

    3. Initialize the open/closed lists and the current_node = start_node

    (Enter Loop Here) 
    
    3.5. Check if the current_node is the end_node
        - If it is, we can just return and exit the code

    4. Add the child nodes of the current_node to the open_list and move the current_node onto the closed_list
        - When adding each node, make sure to calculate each g_cost, h_cost, and f_cost for each node

    5. From the open_list, set the node with the lowest f_cost as the current node and add the current_node to the closed_list

    6. Loop back and repeat the process until we arrive at the end_node

"""

# Define the Node() class
class Node():

    # Set the default constructor of each node
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        # The default g_cost and h_cost values are going to be set to 0
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0

    # Unsquared distance formula
    def distance(self, node_2):
        return abs((node_2.position[0] - self.position[0])**2 + (node_2.position[1] - self.position[1])**2)


# A* implementation
def a_star(matrix, start_pos, end_pos):

    # Define the start node with the input parameters
    start_node = Node(None, start_pos)
    end_node = Node(None, end_pos)

    # Create a deep copy of the start_node and set it as the current_node
    current_node = copy.deepcopy(start_node)

    # Open and closed lists of nodes are initialized as empty (as they should be)
    open_list = []
    closed_list = []

    # Append the current_node (initialized as start_node) onto the open_list so we enter the loop
    open_list.append(current_node)

    # Stay within this loop while we still have potential nearest nodes that need to be visited
    while len(open_list) > 0:

        # Loop through the open_list and if we find a node with a lower f_cost, set it as the current_node
        for x in open_list:
           if x.f_cost < current_node.f_cost:
               current_node = x

        # If our current position is the end position, return
        if(current_node.position == end_pos):
            return

        # Move the current_node onto the closed_list (marking it as visited)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # LIST OF CHILDREN: 

            # (x-1, y+1), (x, y+1), (x+1, y+1)
            # (x-1, y), (parent_node), (x+1, y)
            # (x-1, y-1), (x, y-1), (x+1, y+1)

        # Initialize an empty list of child_nodes
        child_nodes = []

        # Generate child nodes in a creative as fuck method
        for i in range(-1, 2):
            for j in range(-1, 2):

                # Current (x,y) positions
                current_x = current_node.position[0]
                current_y = current_node.position[1]

                # If i, j == 0 this represents position (x,y) so we skip it
                if (i == 0 and j == 0):
                    continue

                # Check if the child's x,y values are not in the matrix's bounds
                if (current_x + i < 0 or current_x + i > len(matrix[0]) or current_y + j < 0 or current_y + j > len(matrix)):
                    continue

                # Create the new child_node and calculate its costs
                child_node = Node(current_node, (current_x + i, current_y + j))

                # Calculate the child node's g_cost, h_cost, and f_cost
                child_node.g_cost = current_node.g_cost + 1
                child_node.h_cost = child_node.distance(end_node)
                child_node.f_cost = child_node.g_cost + child_node.h_cost

                # Append the child_node into the list holding all child_nodes
                child_nodes.append(child_node)

        for child in child_nodes:

            # First, check if the child_node is in the closed_list
            for closed_node in closed_list:
                if closed_node == child:
                    continue

            # Second, check if the child is a part of the open_list already. If it is, compare g_costs
            for open_node in open_list:

                if open_node == child and open_node.g_cost < child.g_cost:
                    continue

            # At this point, we know:
            #   a) The child_node is within the bounds of the matrix.
            #   b) The child_node is NOT closed. (ie: has not been visited)
            #   c) If the child_node is already in the open_list, this one has a lower g_cost

            open_list.append(child)


# Main run() function
def run():

    # TO DO: Define the matrix variable by window size
    matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # TO DO: Define start and end positions according to user input, currently hard coded as (0,0) and (5,5)
    start_position = (0,0)
    end_position = (5,5)

    # Call the A* function
    a_star(matrix, start_position, end_position)

    # Create the main window object and set some parameters
    window = Tk()
    window.title("A* Visualization")
    window.geometry("900x675")

    # Open up the main window :)
    window.mainloop()

# Name check, call the main run function
if __name__ == '__main__':
    run()