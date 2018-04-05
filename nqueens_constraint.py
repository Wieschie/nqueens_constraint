from constraint import *

problem = Problem()

board_size = 10

queen_list = range(board_size)
# enforce different columns by restricting each queen to only move within 1 column.
coord_list = [[(x,y) for y in range(board_size)] for x in range(board_size)]

for q,c in zip(queen_list, coord_list):
    problem.addVariable(q, c)

for queen_1 in queen_list:
    for queen_2 in queen_list:
        if queen_1 < queen_2:
            # must be in different rows
            problem.addConstraint(lambda q1, q2: q1[1] != q2[1], (queen_1, queen_2))
            # cannot be diagonal
            problem.addConstraint(lambda q1, q2: abs(q1[0]-q2[0]) != abs(q1[1]-q2[1]), (queen_1, queen_2))


solutions = problem.getSolutions()

def print_horiz_line():
    print(" ---" * board_size)

for i,s in enumerate(solutions):
    print(f"\n\nSolution {i+1}")
    for y in range(board_size):
        print_horiz_line()
        for x in range(board_size):
            cell = "|   "
            for c in s.values():
                if c == (x,y):
                    cell = f"| Q "
                    break
            print(cell, end='')
        print("|   ")
    print_horiz_line()
