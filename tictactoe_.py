# Tic-Tac-Toe
import random
from termcolor import colored
import time

print(colored("Welcome to Tic-Tac-Toe by Stana and Elias!", "magenta"))
time.sleep(1)
print(colored("Hint: After you entered the player names you can end the game by typing 'exit'.", "magenta")) 
time.sleep(1)

game_active = True

# Gameboard als Liste erstellen
gameboard = [" ",
             colored("1", "black", "on_white"), colored("2","black", "on_white"), colored("3", "black", "on_white"),
             colored("4", "black", "on_white"), colored("5", "black", "on_white"), colored("6", "black", "on_white"),
             colored("7", "black", "on_white"), colored("8", "black", "on_white"), colored("9", "black", "on_white"),
             ]

# Gameboard Ausgabe definieren
def display_gameboard():
    print(colored("\nCurrent Gameboard:\n", "magenta"))
    print(gameboard[1] + "|" + gameboard[2] + "|" + gameboard[3])
    print(gameboard[4] + "|" + gameboard[5] + "|" + gameboard[6])
    print(gameboard[7] + "|" + gameboard[8] + "|" + gameboard[9])


# Spieleingabe und Kontrolle der Eingabe
def player_input():
    global game_active
    while True:
        game_move = input(generate_color_message("Please choose a field: ")).lower()

        if game_move == 'exit':
            # Spieler kann das Spiel mit "exit" beenden
            game_active = False
            print(colored("\nA pity, goodbye!","magenta"))
            return

        error_message = generate_color_message("Your input must be a number between 1 and 9.")

        try:
            # Input in Nummer umwandeln mit Error Handling bei unpassender Eingabe
            game_move = int(game_move)
            if game_move >= 1 and game_move <= 9:
                if gameboard[game_move] == player1_symbol or gameboard[game_move] == player2_symbol:
                    print("Field already taken - please choose another one!")
                else:
                    return game_move
            else:
                raise Exception()

        except Exception:
            print(error_message)


#Spielerwechsel nach einem Zug
def switch_player(player1, player2):
    global active_player
    if active_player == player1:
        active_player = player2
    else:
        active_player = player1
        
              
# Kontrolle, ob ein Spieler gewonnen hat
def victory_check():
    # wenn alle 3 Felder, entweder horizontal, vertikal oder diagonal, gleich sind , hat der entsprechende Spieler gewonnen
    # Kontrolle auf Reihen (horizontal)
    if gameboard[1] == gameboard[2] == gameboard[3]:
        return gameboard[1]
    if gameboard[4] == gameboard[5] == gameboard[6]:
        return gameboard[4]
    if gameboard[7] == gameboard[8] == gameboard[9]:
        return gameboard[7]
    # Kontrolle auf Spalten (vertikal)
    if gameboard[1] == gameboard[4] == gameboard[7]:
        return gameboard[1]
    if gameboard[2] == gameboard[5] == gameboard[8]:
        return gameboard[2]
    if gameboard[3] == gameboard[6] == gameboard[9]:
        return gameboard[3]
    # Kontrolle auf Diagonalen
    if gameboard[1] == gameboard[5] == gameboard[9]:
        return gameboard[5]
    if gameboard[7] == gameboard[5] == gameboard[3]:
        return gameboard[5]

#Kontrolle, ob das Spiel untentschieden ausgegangen ist
def tie_check():
    if (gameboard[1] == player1_symbol or gameboard[1] == player2_symbol) \
            and (gameboard[2] == player1_symbol or gameboard[2] == player2_symbol) \
            and (gameboard[3] == player1_symbol or gameboard[3] == player2_symbol) \
            and (gameboard[4] == player1_symbol or gameboard[4] == player2_symbol) \
            and (gameboard[5] == player1_symbol or gameboard[5] == player2_symbol) \
            and (gameboard[6] == player1_symbol or gameboard[6] == player2_symbol) \
            and (gameboard[7] == player1_symbol or gameboard[7] == player2_symbol) \
            and (gameboard[8] == player1_symbol or gameboard[8] == player2_symbol) \
            and (gameboard[9] == player1_symbol or gameboard[9] == player2_symbol):
        return ('Tie')


#Farben der Spieler festlegen
player1_color = "blue"
player2_color = "green"

#Funktion zum Spielernamen Eingeben
def playernames():
    print()
    player1 = input(colored("Enter a name for player 1 (x): ", player1_color, ))
    player2 = input(colored("Enter a name for player 2 (o): ", player2_color, ))

    return player1, player2

            
# Gamboard ausgeben,Spielernamen eingeben, Start-Spieler zufällig auswählen
display_gameboard()
player1, player2 = playernames()
active_player = random.choice([player1, player2])

#Funktion um Text in Frabe des aktiven Spielers auszugeben
def generate_color_message(message):
    if active_player is player1:
        return colored(message, player1_color, )
    else:
        return colored(message, player2_color, )

def print_player_message(message):
    print(generate_color_message(message))

player1_symbol = generate_color_message(colored("x", player1_color, "on_black"))
player2_symbol = generate_color_message(colored("o", player2_color, "on_black"))

#Hauptloop des Spiels
while game_active:
    print()
    print(generate_color_message(active_player + ", it is your turn!")) #Hinweis wer an der Reihe ist
    game_move = player_input()
    if game_move: #Spielzug ins Gameboard eintragen
        if active_player is player1:
            player_value = player1_symbol
        else:
            player_value = player2_symbol

        gameboard[game_move] = player_value
        # aktuelles gameboard ausgeben
        display_gameboard()
        # Kontrolle, ob jemand gewonnen hat
        victory = victory_check()
        if victory:
            winner = None
            if (victory == player1_symbol):
                winner = player1
            else:
                winner = player2

            print(colored("\nCongrats, '" + winner + "' won!", "magenta"))

            game_active = False
            break
        # Kontrolle, ob tie
        tie = tie_check()
        if tie:
            print(colored("\nIt's a tie! Do it again?", "magenta"))
            game_active = False
        # Spieler wechseln
        switch_player(player1, player2)
