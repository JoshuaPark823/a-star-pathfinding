from tkinter import Tk, Frame, StringVar, Entry, Label, LEFT, Button, RAISED
from a_star_pathfinding import a_star
import generate_matrix
from functools import partial

# Main run() function
def run():

    # Generate an empty 25 x 25 matrix
    matrix = generate_matrix.generate_empty(25,25)

    # Create the main window object and set some parameters
    window = Tk()
    window.title("A* Visualization")

    # Add a frame for the "Run A*" button
    bottom_frame = Frame(master = window, borderwidth = 1)
    bottom_frame.grid(row = len(matrix) + 2, columnspan = len(matrix[0]))

    # Add a frame for the start_position and end_position prompts
    prompt_frame = Frame(master = window, borderwidth = 1, width = 100)
    prompt_frame.grid(row = len(matrix) + 1, column = 0, columnspan = len(matrix[0]))

    # Prompt and label for the start_position
    start_var = StringVar()
    start_var.set("Enter Start Position as x,y: ")
    start_label = Label(master = prompt_frame, textvariable = start_var)
    start_label.pack(side = LEFT)
    start_prompt = Entry(master = prompt_frame)
    start_prompt.pack(side = LEFT)
    end_var = StringVar()
    end_var.set("Enter End Position as x,y: ")
    end_label = Label(master = prompt_frame, textvariable = end_var)
    end_label.pack(side = LEFT)
    end_prompt = Entry(master = prompt_frame)
    end_prompt.pack(side = LEFT)

    # Define a Storage class to hold the return value of the button's callback function, a_star()
    class Storage:

        def __init__(self):
                self.value = []

        def calc_path(self):

            temp1 = (tuple)(start_prompt.get().split(","))
            temp2 = (tuple)(end_prompt.get().split(","))

            start_position = ((int)(temp1[0]), (int)(temp1[1]))
            end_position = ((int)(temp2[0]), (int)(temp2[1]))

            self.value = a_star(matrix, start_position, end_position)

            # Colour the path blue
            for i in range(1, len(self.value)-1):
                widgets[self.value[i]].config(bg = "blue")

            widgets[start_position].config(bg = "black")
            widgets[end_position].config(bg = "red")

    # Create an instance of our Storage class
    storage = Storage()

    # Note, the button calls our Storage class's method calc_path() which calls a_star()
    btn = Button(master = bottom_frame, text = "Run A* Algorithm", command = storage.calc_path)
    btn.pack()

    label_padding = 10

    # Empty dictionary of widgets so we can reference each widget by its tuple key later on
    widgets = {}

    # callback function for clicking on the grid cells
    def callback(event):

        # Change the cell's colour and print it's tuple key for debugging
        event.widget.config(bg = "grey")

        # position tuple normally returns (y,x)
        position_tuple = tuple(widgets.keys())[list(widgets.values()).index(event.widget)]
        position_tuple_x = position_tuple[0]
        position_tuple_y = position_tuple[1]

        matrix[position_tuple_x][position_tuple_y] = 1

    # Step 1
    for i in range(len(matrix)): #loops through rows

        window.columnconfigure(i, weight = 1, minsize = label_padding)
        window.rowconfigure(i, weight = 1, minsize = label_padding)

        # loops through columns
        for j in range(len(matrix[i])):

             # Create a frame object and move it in a grid position onto the window
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
                pady = 0.25 * label_padding # Vertical padding is at 50% reduced scale
            )
            label.bind("<Button-1>", callback)
            label.pack()

            # If the cell is untraversable terrain, colour it grey instead
            if(matrix[j][i] == 1):
                label.config(bg = "grey")

            # Add the tuple defining the position of the cell into the widgets list
            # Now if we wanna access the specific label, we just have to grab it from
            # the widgets dictionary with the tuple key. Sets the widjets index as the
            # label's position in memory.

            widgets[(i,j)] = label

    # Main loop
    window.mainloop()

# Name check, call the main run function
if __name__ == '__main__':
    run()