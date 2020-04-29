from tkinter import *
from a_star_pathfinding import *

"""
The Plan:

    1. Loop through the matrix and display each position with .grid() method
        - Set the start and end nodes as black and red

    2. Run the a_star() algorithm which returns a list of tuples
        - As the algorithm is running, have it's f_cost, g_cost, and h_cost displayed (if non zero)
        - Might need to input the frame or window into the a_star() method and do it there

    3. Highlight the path as the final path

"""

# Main run() function
def run():

    # TO DO: Define the matrix variable by user input
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
    end_position = (5,8)

    # Create the main window object and set some parameters
    window = Tk()
    window.title("A* Visualization")

    label_padding = 25

    # Empty dictionary of widgets so we can reference each widget by its tuple key later on
    widgets = {}

    # Step 1
    for i in range(len(matrix)):

        window.columnconfigure(i, weight = 1, minsize = label_padding)
        window.rowconfigure(i, weight = 1, minsize = label_padding)

        for j in range(len(matrix[i])):

             # Create a frame object and pack it onto the window
            frame = Frame(
                master = window,
                relief = RAISED,
                borderwidth = 1,
                bg = "white"
            )
            frame.grid(row = i, column = j)

            # Label has to be padded to fit the config size, interesting
            label = Label(
                master = frame, 
                text = "", 
                bg = "white",
                padx = label_padding, 
                pady = 0.5 * label_padding # Vertical padding is at 50% reduced scale
            )
            label.pack()

            # If the cell is untraversable terrain, colour it grey instead
            if(matrix[i][j] == 1):
                label.config(bg = "grey")

            # Add the tuple defining the position of the cell into the widgets list
            # Now if we wanna access the specific label, we just have to grab it from
            # the widgets dictionary with the tuple key. Sets the widjets index as the
            # label's position in memory.
            
            widgets[(i,j)] = label

    # Set the start and end node widgets as a diff colour
    widgets[start_position].config(bg = "black")
    widgets[end_position].config(bg = "red")
    

    # Step 2
    path_tuples = a_star(matrix, start_position, end_position)
    
    # highlight the path (minus end nodes) in the gui
    for i in range(1, len(path_tuples)-1):
        widgets[path_tuples[i]].config(bg = "blue")

    # DEBUG aid
    # grid_location(x,y) => returns grid position at pixels (x,y)
    print(window.grid_location(26, 51))
    print(widgets.items())
    print(path_tuples)

    # Main loop
    window.mainloop()


# Name check, call the main run function
if __name__ == '__main__':
    run()