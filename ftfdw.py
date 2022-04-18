calls = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]

matrices = []

with open('datajustboards.txt') as f:
    lines = [ line.rstrip() for line in f ]
    for line in lines:
        if line == '':
            matrices.append([])
        else:
            matrices[-1].append([int(num.rstrip()) for num in line.split(" ") if not num == ''])

five_by_five = [[0 for i in range(5)] for j in range(5)]
game_board = [five_by_five for k in range(len(matrices))]

# game_board => 0 -> unmarked, 1 -> marked

for call in calls:
    # print(game_board)
    for i in range(len(matrices)):
        unmarked_sum = 0
        for row in range(5):
            for col in range(5):
                if matrices[i][row][col] == call:
                    # mark it
                    game_board[i][row][col] = 1

                # If the cell is not marked
                if game_board[i][row][col] == 0:
                    unmarked_sum += matrices[i][row][col]

        possible_result = call * unmarked_sum

        for row_num in range(5):
            all_ones_in_row = True
            for col_num in range(5):
                if game_board[i][row_num][col_num] == 0:
                    all_ones_in_row = False

            if all_ones_in_row:
                print(possible_result)
                exit(0)

        for col_num in range(5):
            all_ones_in_col = True
            for row_num in range(5):
                if game_board[i][row_num][col_num] == 0:
                    all_ones_in_col = False

            if all_ones_in_col:
                print(possible_result)
                exit(0)