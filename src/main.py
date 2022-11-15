from board import Board

# fileName = input('File name containing the board information to initialize the board: ')
fileName = 'test.txt'
file = open('./static/' + fileName, "r")

for line in file:
    if line[0] == '#' or line == "\n":
        continue
    board_fuel = line.strip().split(" ")
    board = Board(list(board_fuel[0]), board_fuel[1:])

