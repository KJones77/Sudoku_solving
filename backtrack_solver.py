
""" example of a board as a 2d array
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0]
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
                        
# A backtracking algorithm class to solve sudoku boards

class Backtrack_Solver(object):
    def __init__(self):
        # initialize a class variable 1-9 set to be used for later calculations
        self.full_key = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Prints the board in more readable way
    def print_board(self, board):
        FIRST_GROUP  = [0, 3]
        SECOND_GROUP = [3, 6]
        THIRD_GROUP  = [6, 9]
        GROUPS = [FIRST_GROUP, SECOND_GROUP, THIRD_GROUP]
        print("|-----------------------|")
        print("| ", end = "")

        for row in range(9):
            for col in range(9):
                if (col == 3 or col == 6):
                    print("| ", end = "")
                
                print (str(board[row][col]) + " ", end = "")

            if (row == 2 or row == 5):
                print("|\n|-----------------------|\n| ", end = "")
            elif (row != 8):
                print("| \n| ", end = "")
            else:
                print("| \n|", end = "")

        print("-----------------------|")
       
        return None


    # Finds which local box on a sudoku board a given set of row,col coordinates lies in
    # then returns the coordinates of top left cell of the box as a tuple (row, col)
    def get_local_box(self, row_index = -1, col_index = -1):
        if (row_index < 0 or col_index < 0):
            print("invalid row or column index passed into get_local_box()")
            return None

        box_row = -1
        box_col = -1

        """ coordinate bounds of the local boxes
                0-2, 0-2 (top left)      [0, 0]
                0-2, 3-5 (top middle)    [0, 3]
                0-2, 6-8 (top right)     [0, 6]
                3-5, 0-2 (middle left)   [3, 0]
                3-5, 3-5 (middle middle) [3, 3]
                3-5, 6-8 (middle right)  [3, 6]
                6-8, 0-2 (bottom left)   [6, 0]
                6-8, 3-5 (bottom middle) [6, 3]
                6-8, 6-8 (bottom right)  [6, 6]
        """
        # If the row index is 0-2 then the given cell is somewhere in the top row of boxes
        if (row_index < 3):
            box_row = 0
        # else if the row index is 3-5 then the given cell is somewhere in the middle row of boxes
        elif(row_index > 2 and row_index < 6):
            box_row = 3
        # else if the row index is 6-8 then the given cell is somewhere in the bottom row of boxes
        elif (row_index > 5 and row_index < 9):
            box_row = 6
        
        # If the column index is 0-2 then the given cell is somewhere in the left column of boxes
        if (col_index < 3):
            box_col = 0
        # else if the column index is 3-5 then the given cell is somewhere in the middle column of boxes
        elif(col_index > 2 and col_index < 6):
            box_col = 3
        # else if the column index is 6-8 then the given cell is somewhere in the right column of boxes
        elif (col_index > 5 and col_index < 9):
            box_col = 6
        return [box_row, box_col]
        
        
    # Gets all potential values for any given cell
    # returns a set of the potential values for a given cell
    def get_potential_vals(self, board = None, row_ind = 0, col_ind = 0):
        possible_vals = set() # all possible values for the cell at row_ind, col_ind on board
        curr_row_vals = set() # a set representation of all values in the row at row_ind on the current board
        curr_col_vals = set() # a set representation of all values in the col at col_ind on the current board
        curr_box_vals = set() # a set representation of all values in the local box of the cell at (row_ind, col_ind)
        curr_box = []         # row, col representation of the coordinates of the top leftmost corner cell of the current cell's local box
        
        # put all values of the current row into a set
        if (type(board[row_ind]) is list):
            curr_row_vals = set(board[row_ind])
        else:
            return None

        # put all values of the current col into a set
        if (type(board[col_ind]) is list):
            for i in range(9):
                curr_col_vals.add(board[i][col_ind])
        else:
            return None

        # find the local box the given cell resides in and
        # get all potential values for that box
        curr_box = self.get_local_box(row_ind, col_ind)
        

        # loop through a 3x3 local box on the board starting from the top left corner cell
        # and add each value from each cell in that local box into a the curr_box_vals set
        for i in range(3):
            for j in range(3):
                curr_box_vals.add(board[curr_box[0] + i][curr_box[1] + j])
        

        # Get set difference between curr_row and all values 1-9
        possible_vals = self.full_key.difference(curr_row_vals)

        # Get set difference between curr_col and possible_vals
        possible_vals.difference_update(curr_col_vals)

        # Get set difference between curr_box and possible_vals
        possible_vals.difference_update(curr_box_vals)

        return possible_vals

    """ 
    A recursive backtracking algorithm function to solve sudoku boards
        board is a 2d array, board[row][col] (start_row, start_col) are the coordinates for the 
        cell where this instance of the backtrack_solve function will begin

    Input: board = 2d array representing a valid sudoku board with empty spaces = 0
           start_row/start_col = an integer representing the coordinates for the starting position of the current call to backtrack_solve

    Output: returns boolean value to determine if the board is finished solving or not
    """
    def backtrack_solve(self, board = None, start_row = 0, start_col = 0):
        # Check if a board was even passed into the function
        if (board == None):
            print("Try again you did not enter a board")
            return None
        poten_vals = set()                          # all potential values for the current cell as a set
        is_solved = False                           # boolean flag to check if the board is solved or not
        curr_cell_val = board[start_row][start_col] # holds the value of the current cell
        nxt_row = start_row                         # the row value of the next cell in the board to be looked at
        nxt_col = start_col                         # the col value of the next cell in the board to be looked at

        # If we are on the last column
        # move down one row and set the column to the first column
        # otherwise move the column to the right
        if (nxt_col == 8):
            nxt_col = 0
            nxt_row += 1
        else:
            nxt_col += 1

        
        # check if current cell already has a number in it if so then move on to the next cell
        # on the board and return that function call
        if (curr_cell_val != 0):
            return self.backtrack_solve(board, nxt_row, nxt_col)

        # get all possible values for the current cell
        poten_vals = poten_vals.union(self.get_potential_vals(board, start_row, start_col))



        # if last cell in the board and there is a potential value then return True
        if (nxt_row == 9 and len(poten_vals) == 1):
            board[start_row][start_col] = poten_vals.pop()
            is_solved = True

        #poten_vals.discard(0)
        # repeat the loop until the puzzle is solved
        while (is_solved == False and len(poten_vals) > 0):

            # insert one of the remaining potential values into the current position on the board
            # and remove it from the set of potential values
            board[start_row][start_col] = poten_vals.pop()

            # set is solved = to a call to the backtrack solver function with new board and the next cell's coordinates
            is_solved = self.backtrack_solve(board, nxt_row, nxt_col)

        # if all the potential values for the current position failed
        # then reset the current positons value to zero
        if (is_solved is False):
            board[start_row][start_col] = 0

        return is_solved
        