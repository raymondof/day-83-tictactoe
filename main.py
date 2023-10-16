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

game = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
print(field)
game["2"] = "x"
print(game)

game_on = True
player = 1
while game_on:
    mark = input(f"Player {player} place your mark with numbers 1-9.")
    # Check if input is numerical and convert it to integer
    if mark.isnumeric():
        mark = int(mark)
    else:
        print("Please enter numerical value")
        continue
    if mark < 0 and mark > 10:
        print("ok")
    else:
        print("Please enter number from 1 to 9.")
