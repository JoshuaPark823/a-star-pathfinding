# A* Pathfinding Algorithm Visualization 🔎

## Overview: 

- As I'm sure you're well aware of what the A* pathfinding algorithm is, I won't go into too much detail.
Basically, A* is a variant of Dijkstra's algo, and uses inherent movements costs to decide its 
node traversal. These costs (g, h, and f) are the distance from the current node to the start node, 
the distance from the current node to the end node (calculated from a heuristic), and the sum of the
the g and h costs above.

- The algorithm avoids dynamically placed obstacles and finds the most optimal path to the end node, taking into account the varying distances.

## Roadblocks! 😱

1. First Roadblock (GUI):
	- The first issue that I've come across is with the GUI. Currently I have it set up so that
	two for loops are nested (representing x and y values) and in the body of the inner loop I 
	instantiate the `Frame` objects and the `Label` objects. I'm storing the references to each
	label in an empty dictionary instantiated outside the loops. 
	- I want to change the colour of individual cells once outside the loop by using their tuples
	as indexes and accessing their attributes but nothing's been working.

2. Second Roadblock (Storing Callback Return Value):
	- I realized that having `a_star()` called from the button's `command` attribute is a horrible 
	idea because the return value, aka the path, won't be accessible.

## Solutions 🥳

1. Extremely simple and obvious solution. All I had to do was write `widgets[position].config(bg = "...")`.
I believe the reason I had trouble is because I wasn't as familiar with TKinter's API. So after reading some
more documentation and exhausting every stackoverflow page in existence, I got a better understanding of 
widget hierarchy! (Solved)

2. This actually took a surprisingly long amount of time to figure out but I defined a `Storage` class that
has a list attribute. I then created an instance method for this class that calls `a_star()` and stores the
return value in `self.value` (the attribute).
	- Note: I could've easily used a global variable to hold my button callback function's return value
	**BUT** using global variables to store values is **bad practice** and harder to manage. 
	Therefore, I stored it in a class's fields :)

## Languages, Tools, & Technologies 🛠
- Python 3.8.3
- Tkinter API

![Screenshot](./a_star_gui_sc.png)



