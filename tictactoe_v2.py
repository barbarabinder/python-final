# Spiel Tic-Tac-Toe
import random
from termcolor import colored

print(colored("Tic-Tac-Toe Python Tutorial", "magenta"))
spiel_aktiv = True

# Spielfeld als Liste erstellen
spielfeld = [" ",
             colored("1", "black", "on_white"), colored("2","black", "on_white"), colored("3", "black", "on_white"),
             colored("4", "black", "on_white"), colored("5", "black", "on_white"), colored("6", "black", "on_white"),
             colored("7", "black", "on_white"), colored("8", "black", "on_white"), colored("9", "black", "on_white"),
             ]

# Spielfeld ausgeben
def spielfeld_ausgeben():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])


# Spieleingabe und Kontrolle der Eingabe
def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input(generate_color_message(spieler_aktuell + ", bitte wähle ein Feld: "))

        if spielzug == 'exit':
            # Spieler beendet das Spiel
            spiel_aktiv = False
            return

        error_message = generate_color_message("Zahl muss zwischen 1 und 9 liegen")

        try:
            # Input in Nummer umwandeln
            spielzug = int(spielzug)
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == spieler1_symbol or spielfeld[spielzug] == spieler2_symbol:
                    print("Das Feld ist bereits belegt - ein anderes wählen!")
                else:
                    return spielzug
            else:
                raise Exception()

        except Exception:
            print(error_message)



def spieler_wechseln(spieler1, spieler2):
    global spieler_aktuell
    if spieler_aktuell == spieler1:
        spieler_aktuell = spieler2
    else:
        spieler_aktuell = spieler1


# Kontrolle, ob ein Spieler gewonnen hat
def kontrolle_gewonnen():
    # wenn alle 3 Felder gleich sind, hat der entsprechende Spieler gewonnen
    # Kontrolle auf Reihen
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    # Kontrolle auf Spalten
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    # Kontrolle auf Diagonalen
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[5]
    if spielfeld[7] == spielfeld[5] == spielfeld[3]:
        return spielfeld[5]


def kontrolle_auf_unentschieden():
    if (spielfeld[1] == spieler1_symbol or spielfeld[1] == spieler2_symbol) \
            and (spielfeld[2] == spieler1_symbol or spielfeld[2] == spieler2_symbol) \
            and (spielfeld[3] == spieler1_symbol or spielfeld[3] == spieler2_symbol) \
            and (spielfeld[4] == spieler1_symbol or spielfeld[4] == spieler2_symbol) \
            and (spielfeld[5] == spieler1_symbol or spielfeld[5] == spieler2_symbol) \
            and (spielfeld[6] == spieler1_symbol or spielfeld[6] == spieler2_symbol) \
            and (spielfeld[7] == spieler1_symbol or spielfeld[7] == spieler2_symbol) \
            and (spielfeld[8] == spieler1_symbol or spielfeld[8] == spieler2_symbol) \
            and (spielfeld[9] == spieler1_symbol or spielfeld[9] == spieler2_symbol):
        return ('unentschieden')


spieler1_color = "blue"
spieler2_color = "green"
def spielernamen():
    print()
    spieler1 = input(colored("Bitte Namen eingeben für SpielerIn 1: ", spieler1_color, "on_black"))
    spieler2 = input(colored("Bitte Namen eingeben für SpielerIn 2: ", spieler2_color, "on_black"))

    return spieler1, spieler2


# Spieler
spielfeld_ausgeben()
spieler1, spieler2 = spielernamen()
spieler_aktuell = random.choice([spieler1, spieler2])


def generate_color_message(message):
    if spieler_aktuell is spieler1:
        return colored(message, spieler1_color, "on_black")
    else:
        return colored(message, spieler2_color, "on_black")

def print_player_message(message):
    print(generate_color_message(message))

spieler1_symbol = generate_color_message(colored("x", spieler1_color, "on_black"))
spieler2_symbol = generate_color_message(colored("o", spieler2_color, "on_black"))

while spiel_aktiv:
    # Eingabe des aktiven Spielers
    print()
    print(generate_color_message("Spieler '" + spieler_aktuell + "' am Zug -"))
    spielzug = spieler_eingabe()
    if spielzug:

        if spieler_aktuell is spieler1:
            spieler_value = spieler1_symbol
        else:
            spieler_value = spieler2_symbol

        spielfeld[spielzug] = spieler_value
        # aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        # Kontrolle, ob jemand gewonnen hat
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            gewinner = None
            if (gewonnen == spieler1_symbol):
                gewinner = spieler1
            else:
                gewinner = spieler2

            print(colored("Spieler '" + gewinner + "' hat gewonnen!", "magenta"))

            spiel_aktiv = False
            break
        # Kontrolle, ob unentschieden
        unentschieden = kontrolle_auf_unentschieden()
        if unentschieden:
            print("Spiel ist unentschieden ausgegangen")
            spiel_aktiv = False
        # Spieler wechseln
        spieler_wechseln(spieler1, spieler2)
print()
spielfeld_ausgeben()