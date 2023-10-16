print("Welcome to play Tic Tac Toe. This is a simple text based game created by Raimo.")
print("It will allow 2 players to play.\n")
print("Each player will turn after each other.")
print("First player is 'X' and second player 'O'. The first to gain 3 straight line wins!")
print("Good luck!")

field = """
7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3
"""

game = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
print(field)

def check_winner(board, mark):
    hor_count = 0
    mark_counter = 0
    print(f"Players mark: {mark}")

    for key, value in board.items():
        if value != "":
            mark_counter += 1
        # Horizontal counter
        # Reset horizontal counter at the beginning of each horizontal line
        if key == 4 or key == 7:
            hor_count = 0
        # If the current place on board (value) has mark count it in the horizontal counter
        if value == mark:
            hor_count += 1
            if hor_count == 3:
                return 1

        # Vertical checker
        if value == mark and key > 0 and key < 4:
            vertical_start = key
            next_value = vertical_start + 3
            if board[next_value] == mark:
                next_value = vertical_start + 6
                if board[next_value] == mark:
                    return 1

        # Diagonal checker
        #if value == mark and key == 1 or value == mark and key == 3:
            diagonal_start = key
        if value == mark and key == 1:
            if board[5] == mark:
                if board[9] == mark:
                    return 1
        elif value == mark and key == 3:
            if board[5] == mark:
                if board[7] == mark:
                    return 1

        # Draw checker
        if mark_counter == 9:
            return 0




game_on = True
players = {1: "X", 2: "O"}
player = 1
while game_on:
    mark = input(f"Player {player} place your mark with numbers 1-9: ")
    # Check if input is numerical and convert it to integer
    if mark.isnumeric():
        mark = int(mark)
    else:
        print("Please enter numerical value")
        continue

    if mark > 0 and mark < 10:
        if game[mark] == "":
            game[mark] = players[player]
            #print(game)
            field = field.replace(str(mark), players[player])
            result = check_winner(game, players[player])
            print(field)

            if result == 1:
                print(f"Player {player} has won the game")
                break
            elif result == 0:
                print("No winner this time!")
                break

            # Change player
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print("Choose another spot, this is taken!")

    else:
        print("Please enter number from 1 to 9.")
