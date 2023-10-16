print("Welcome to play Tic Tac Toe. This is a simple text based game created by Raimo.")
print("It will allow 2 players to play.\n")
print("The game field is as follows. Each player will get one turn.")
print("First player is 'X' and second player 'O'")

field = """
7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3
"""

game = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
print(field)
#game["2"] = "x"
print(game)

def check_winner(board, mark):
    current = 1
    hor_count = 0
    print(f"Players mark: {mark}")

    for key, value in board.items():
        print(key, value)
        current += 1

        # Horizontal cunter
        # Reset horizontal counter at the beginning of each horizontal line
        if key == 4 or key == 7:
            hor_count = 0
        # If the current place on board (value) has mark count it in the horizontal counter
        if value == mark:
            hor_count += 1
            if hor_count == 3:
                return 1

        # Vertical counter



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
            print(game)
            field = field.replace(str(mark), players[player])
            print(field)
            result = check_winner(game, players[player])

            if result == 1:
                print(f"Player {player} has won the game")
                print("Game over!")
                break

            # Change player
            if player == 1:
                player = 2
            else:
                player = 1

    else:
        print("Please enter number from 1 to 9.")
