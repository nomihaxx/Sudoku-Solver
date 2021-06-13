import os

attempts = 0


def print_board(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(board[x][y])
            else:
                print(str(board[x][y]) + " ", end="")
def find_zero(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None

def is_valid(board, row, col, value):
    #check row
    if value in board[row]:
        return False
    #check column
    for r in board:
        if r[col] == value:
            return False
    #check box
    box_x = row // 3
    box_y = col // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[j][i] == value:
                return False
    return True

def solve(board):
    global attempts
    row, col = find_zero(board)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(board, row, col, guess):
            board[row][col] = guess

    ###############################################################
            '''
            Uncomment the below in order to show the work
            '''
            #os.system('cls')
            #print_board(board)
            #print("Attempt number {}.".format(attempts))
    ###############################################################

            if solve(board):
                return True
        board[row][col] = 0
        attempts += 1
    return False

if __name__ == '__main__':
    board = [
    [0, 4, 0, 0, 3, 0, 8, 7, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 6, 0, 9, 0, 2, 0, 0, 5],
    [1, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 1, 6, 3, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 3],
    [5, 0, 0, 8, 0, 7, 0, 6, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 9, 2, 0, 4, 0, 0, 8, 0]]

    empty_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solve(board)
os.system('cls')
print_board(board)
print("Attempted to solve {} times before finding the solution.".format(attempts))
