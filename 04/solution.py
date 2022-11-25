class BingoBoard:
    '''
    Rows variable will store numbers as follows:
    [   
         [22, 13, 17, 11, 0]
        ,[8, 2, 23, 4, 24]
        ,[21, 9, 14, 16, 7]
        ,[6, 10, 3, 18, 5]
        ,[1, 12, 20, 15, 19]
    ]
    Numbers that have been guess will be replaced with a None value
    '''
    
    def __init__(self):
        self.rows = []            
        self.solved = False

    def add_row(self, row):
        self.rows.append([int(x) for x in row.split(' ')])

    def check_board(self):
        #rows
        for row in self.rows:
            none_count = 0
            for value in row:
                if value is None:
                    none_count += 1
            if none_count == 5:
                self.solved = True

        #columns
        column_list = [[x[i] for x in self.rows] for i in range(0, 5)]
        for column in column_list:
            none_count = 0
            for value in column:
                if value is None:
                    none_count += 1
            if none_count == 5:
                self.solved = True

    def score_board(self):
        board_score = 0
        for row in self.rows:
            board_score += sum(filter(None, row))
        return board_score
    
    def guess_number(self, number):
        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                if value == number:
                    self.rows[i][j] = None


with open('04/input.txt', 'r') as inputfile:
    raw_list = inputfile.read().splitlines()
    cleaned_list = [x.strip().replace('  ',' ') for x in raw_list]

# PART ONE

guess_list = []
board_list = []

for line in cleaned_list:
    if guess_list == []:
        guess_list = [int(x) for x in line.split(',')]
    elif line == '':
        board_list.append(BingoBoard())
    else:
        board_list[len(board_list) - 1].add_row(line)

bingo_called = False

while bingo_called == False and len(guess_list) > 0:
    current_guess = guess_list.pop(0)
    for board in board_list:
        board.guess_number(current_guess)
        board.check_board()
        if board.solved:
            bingo_called = True
            board_score = board.score_board()
            print(f'{current_guess} {board_score} {current_guess * board_score}')

# PART TWO

guess_list = []
board_list = []

for line in cleaned_list:
    if guess_list == []:
        guess_list = [int(x) for x in line.split(',')]
    elif line == '':
        board_list.append(BingoBoard())
    else:
        board_list[len(board_list) - 1].add_row(line)

remaining_boards = len(board_list)

while remaining_boards > 0 and len(guess_list) > 0:
    current_guess = guess_list.pop(0)
    for board in board_list:
        if not board.solved:
            board.guess_number(current_guess)
            board.check_board()
            if board.solved:
                remaining_boards = remaining_boards - 1
                if remaining_boards == 0:
                    board_score = board.score_board()
                    print(f'{current_guess} {board_score} {current_guess * board_score}')
