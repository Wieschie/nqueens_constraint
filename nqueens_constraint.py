from constraint import *

problem = Problem()

board_size = 5
nqueens = 5

var_list = range(nqueens)
var_list = [f"Q{v}" for v in var_list]
# list of tuples for all coordinate locations
coord_list = [(x,y) for x in range(board_size) for y in range(board_size) ]

problem.addVariables(var_list, coord_list)
problem.addConstraint(AllDifferentConstraint())
for queen_1 in var_list:
    for queen_2 in var_list:
        if queen_1 < queen_2:
            # must be in different columns
            problem.addConstraint(lambda q1, q2: q1[0] != q2[0], (queen_1, queen_2))
            # must be in different rows
            problem.addConstraint(lambda q1, q2: q1[1] != q2[1], (queen_1, queen_2))
            # cannot be diagonal
            problem.addConstraint(lambda q1, q2: abs(q1[0]-q2[0]) != abs(q1[1]-q2[1]), (queen_1, queen_2))

solutions = problem.getSolutions()
unique_solutions = set()
for s in solutions:
    unique_solutions.add(frozenset(s.values()))

def print_horiz_line():
    print(" ---" * board_size)

for i,s in enumerate(unique_solutions):
    print(f"\n\nSolution {i}")
    for y in range(board_size):
        print_horiz_line()
        for x in range(board_size):
            cell = "|   "
            for c in s:
                if c == (x,y):
                    cell = f"| Q "
            print(cell, end='')
        print("|   ")
    print_horiz_line()
