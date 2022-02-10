# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean,
# already so deep that you can't see any sunlight. What you can see, however,
# is a giant squid that has attached itself to the outside of your submarine.
#
# Maybe it wants to play bingo?
#
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards
# on which it appears. (Numbers may not appear on all boards.)
# If all numbers in any row or any column of a board are marked, that board wins.
# (Diagonals don't count.)
#
# The submarine has a bingo subsystem to help passengers
# (currently, you and the giant squid) pass the time. It automatically generates a
# random order in which to draw numbers and a random set of boards (your puzzle input).
def get_score_of_winning_board(numbers_drawn, boards):
    # I am assuming there are no 3 digit numbers on the boards,
    # so I'll mark the numbers with 100
    _marked = 100

    for i in range(len(numbers_drawn)):
        print("Number pulled:", numbers_drawn[i])
        for board in boards:
            for j in range(5):
                for k in range(5):
                    if board[j][k] == numbers_drawn[i]:
                        board[j][k] = _marked
                        print(board)

                        if i > 4:
                            row_sum = sum(board[j])
                            col_sum = sum(row[k] for row in board)
                            if row_sum == 500 or col_sum == 500:
                                print("WINNING BOARD!")
                                print(board)
                                total = 0
                                for l in range(5):
                                    for m in range(5):
                                        if board[l][m] != 100:
                                            total += board[l][m]
                                            print(total)
                                return total * numbers_drawn[i]
                        break
    return None


# def get_score_of_last_winning_board(numbers_drawn, boards):
#     # I am assuming there are no 3 digit numbers on the boards,
#     # so I'll mark the numbers with 100
#     _marked = 100
#
#     for i in range(len(numbers_drawn)):
#         print("Number pulled:", numbers_drawn[i])
#         for board in boards:
#             for j in range(5):
#                 for k in range(5):
#                     if board[j][k] == numbers_drawn[i]:
#                         board[j][k] = _marked
#                         print(board)
#
#                         if i > 4:
#                             row_sum = sum(board[j])
#                             col_sum = sum(row[k] for row in board)
#                             if row_sum == 500 or col_sum == 500:
#                                 print("WINNING BOARD!")
#                                 print(board)
#                                 total = 0
#                                 for l in range(5):
#                                     for m in range(5):
#                                         if board[l][m] != 100:
#                                             total += board[l][m]
#                                             print(total)
#                                 return total * numbers_drawn[i]
#                         break
#     return None


if __name__ == "__main__":
    # Read in input
    with open("input.txt", "r") as file:
        # First line is called numbers
        draw_numbers = list(map(int, file.readline().split(',')))
        # Next line will be empty to just get rid of it
        file.readline()
        # Read through the rest to get the bingo boards
        boards_in_play = []
        bingo_board = []
        for line in file:
            # If line is empty the next few lines contain a bingo board
            if line == "\n":
                boards_in_play.append(bingo_board)
                bingo_board = []
            else:
                bingo_board.append(list(map(int, line.split())))
        # Append last bingo board
        boards_in_play.append(bingo_board)
    print("Winning score:", get_score_of_winning_board(draw_numbers, boards_in_play))

    print(
        "Losing score:", get_score_of_last_winning_board(draw_numbers, boards_in_play)
    )
