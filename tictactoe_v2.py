# Spiel Tic-Tac-Toe
import random
from termcolor import colored

print(colored("Tic-Tac-Toe Python Tutorial", "green"))
spiel_aktiv = True
#spieler_aktuell = 'Stana'
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
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == 'X' or spielfeld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt - ein anderes wählen!")
                else:
                    return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")


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
    if (spielfeld[1] == 'X' or spielfeld[1] == 'O') \
            and (spielfeld[2] == 'X' or spielfeld[2] == 'O') \
            and (spielfeld[3] == 'X' or spielfeld[3] == 'O') \
            and (spielfeld[4] == 'X' or spielfeld[4] == 'O') \
            and (spielfeld[5] == 'X' or spielfeld[5] == 'O') \
            and (spielfeld[6] == 'X' or spielfeld[6] == 'O') \
            and (spielfeld[7] == 'X' or spielfeld[7] == 'O') \
            and (spielfeld[8] == 'X' or spielfeld[8] == 'O') \
            and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
        return ('unentschieden')


def spielernamen():
    print()
    spieler1 = input("Bitte Namen eingeben für Spieler 1: ")
    spieler2 = input("Bitte Namen eingeben für Spieler 2: ")

    return spieler1, spieler2


# aktuelles Spielfeld ausgeben
spielfeld_ausgeben()
spieler1, spieler2 = spielernamen()
spieler_aktuell = random.choice([spieler1, spieler2])

while spiel_aktiv:
    # Eingabe des aktiven Spielers
    print()
    print("Spieler " + spieler_aktuell + " am Zug")
    spielzug = spieler_eingabe()
    if spielzug:
        # spielfeld[spielzug] = 'X'
        if spieler_aktuell is spieler1:
            spieler_value = colored("x", "red", "on_black")

        else:
            spieler_value = colored("0", "white", "on_black")

        spielfeld[spielzug] = spieler_value
        # aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        # Kontrolle, ob jemand gewonnen hat
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print("Spieler " + gewonnen + " hat gewonnen!")
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