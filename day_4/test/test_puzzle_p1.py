from puzzle_p1 import get_score_of_winning_board, get_score_of_last_winning_board


def test_get_score_of_winning_board():
    with open("test/sample_input.txt", "r") as file:
        called_nums = list(map(int, file.readline().split(',')))
        # Next line will be empty to just get rid of it
        file.readline()
        # Read through the rest to get the bingo boards
        boards = []
        bingo_board = []
        for line in file:
            # If line is empty the next few lines contain a bingo board
            if line == "\n":
                boards.append(bingo_board)
                bingo_board = []
            else:
                bingo_board.append(list(map(int, line.split())))
        # Append last bingo board
        boards.append(bingo_board)

    assert get_score_of_winning_board(called_nums, boards) == 4512


# def test_get_score_of_last_winning_board():
#     with open("test/sample_input.txt", "r") as file:
#         called_nums = list(map(int, file.readline().split(',')))
#         # Next line will be empty to just get rid of it
#         file.readline()
#         # Read through the rest to get the bingo boards
#         boards = []
#         bingo_board = []
#         for line in file:
#             # If line is empty the next few lines contain a bingo board
#             if line == "\n":
#                 boards.append(bingo_board)
#                 bingo_board = []
#             else:
#                 bingo_board.append(list(map(int, line.split())))
#         # Append last bingo board
#         boards.append(bingo_board)
#
#     assert get_score_of_last_winning_board(called_nums, boards) == 1924
