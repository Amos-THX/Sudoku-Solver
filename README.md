# Sudoku-Solver

# This piece of code solves a Sudoku puzzle using a recursive approach.

# Instructions
Update the variable "board" based on the Sudoku puzzle. 
1) Save all numbers as strings. Save all empty cells as "."
2) Run the entire script.

# Explationation
We use a recursive approach to solve the puzzle. 
The solver loop through every single cell, from position (0,0) to (8,8). 
The solver will find the first available number (from 1-9) that can be placed in the cell. After which it will loop to the next cell and place the first available number. 
Once the solver reaches a point where numbers 1-9 are all wrong i.e. wrong solution, it will reverse back to the previous box and try the next number. 


