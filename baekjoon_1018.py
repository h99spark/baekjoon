row, column = map(int, input().split())
board = []
for _ in range(row):
    board.append(input())

repaint_list = []

for i in range(row-7):
    for j in range(column-7):
        black_board = white_board = 0
        for row8 in range(i, i+8):
            for column8 in range(j, j+8):
                if (row8 + column8) % 2 == 0:
                    if board[row8][column8] != 'W':
                        black_board += 1
                    if board[row8][column8] != 'B':
                        white_board += 1
                else:
                    if board[row8][column8] != 'B':
                        black_board += 1
                    if board[row8][column8] != 'W':
                        white_board += 1
        repaint_list.append(min(black_board, white_board))

print(min(repaint_list))

