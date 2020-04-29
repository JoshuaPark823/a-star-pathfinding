# A* Pathfinding Algorithm Visualization

## Overview: 

- As I'm sure you're well aware of what the A* pathfinding algorithm is, I won't go into too much detail.
Basically, A* is a variant of Dijkstra's algo, and uses inherent movements costs to decide its 
node traversal. These costs (g, h, and f) are the distance from the current node to the start node, 
the distance from the current node to the end node (calculated from a heuristic), and the sum of the
the g and h costs above.

- I implement this algorithm using python and create a graphical user interface and visualization using
tools imported from tkinter.

## Roadblocks!

1. First Roadblock (GUI):
	- The first issue that I've come across is with the GUI. Currently I have it set up so that
	two for loops are nested (representing x and y values) and in the body of the inner loop I 
	instantiate the `Frame` objects and the `Label` objects. I'm storing the references to each
	label in an empty dictionary instantiated outside the loops. 
	- I want to change the colour of individual cells once outside the loop by using their tuples
	as indexes and accessing their attributes but nothing's been working. TBD

## Solutions

- Again no roadblocks this time around. Calm n collected approaches always result in solid implementation.









