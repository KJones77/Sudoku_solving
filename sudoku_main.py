from backtrack_solver import Backtrack_Solver

board1 = [[0, 5, 0, 1, 0, 0, 9, 2, 0],
          [0, 0, 0, 9, 0, 0, 0, 0, 0], 
          [2, 6, 9, 0, 0, 0, 0, 0, 7], 
          [7, 0, 0, 0, 0, 0, 6, 1, 9], 
          [5, 0, 0, 0, 0, 0, 0, 0, 0],
          [6, 2, 4, 0, 0, 0, 0, 0, 5], 
          [3, 0, 6, 0, 0, 0, 0, 7, 2], 
          [0, 0, 2, 0, 0, 5, 0, 9, 0], 
          [9, 4, 5, 0, 0, 1, 0, 3, 0]]

my_solver = Backtrack_Solver()
print("Original board:")
my_solver.print_board(board1)
print("\nSolution board:")
my_solver.backtrack_solve(board1)
my_solver.print_board(board1)
