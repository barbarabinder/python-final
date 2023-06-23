# AI REVIEW: TIC TAC TOE

Folgendes Review analysiert die Coding Fähigkeiten von ChatGPT 3.5 für das Programmieren eines Tic-Tac-Toe Spiels anhand sieben Aspekten.  Dabei wird der AI-generierte Code mit dem menschlich Entwickelten verglichen. 

**Funktionalität:** ChatGPT 3.5 ist in der Lage einen voll-funktionsfähigen code für ein simples Tic-Tac-Toe Spiel zu generieren, der alle unsere vordefinierten Requirements (Spielfeld in Python Shell ausgeben, Zwei-Spieler Modus, Spielernamen eingeben) erfüllt. 
Somit stimmt die Ausgabe grundsätzlich mit den gestellten Erwartungen überein, obwohl der Stil des Codes zum größten Teil starke Unterschiede aufweist. 

**Datentypen und Variablennamen:** Der generierte Code verwendet durchgehend sinnvolle Datentypen sowie passende Variablen. 

**Übersichtlichkeit und Struktur:** Der Code ist logisch strukturiert, übersichtlich und leicht verständlich. 
Es werden klar benannte Funktionen in sinnvoller Reihenfolge für die notwendigen Operationen verwendet sowie Abstände zwischen IF-blöcken oder Loops integriert, die für eine klare visuelle Übersicht sorgen. 

**Effizienz:** Der Code weist keine Redundanzen auf und ist im Vergleich zu unserem selbst entwickelten Programm teilweise sogar effizienter gestaltet. 
Am besten lässt sich dies im Vergleich des „Win-Checks“ und des „Tie Checks“ illustrieren: 

Selbstentwickelt: 
      
      def victory_check():
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

ChatGPT: 
        
        def check_win(board):
            # Check rows
            for row in board:
                if len(set(row)) == 1 and row[0] != " ":
                    return row[0]
            # Check columns
            for col in range(3):
                if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != " ":
                    return board[0][col]
            # Check diagonals
            if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != " ":
                return board[0][0]
            if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != " ":
                return board[0][2]
        
        Code für ein „Tie“: 
               elif moves == 9:
                    print_board(board)
                    print("It's a tie!")
                    break

Wie zu erkennen ist für vor allem der Code für das „Tie“ Ergebnis von ChatGPT deutlich effizienter. 
Optimierungspotentiale können v.a. beim Error Handling gefunden werden. Der Code von ChatGPT ist zum Beispiel nicht auf jede Art von Input der Spieler vorbereitet, weshalb der Code bei vielen (ungeplanten) Inputs seitens der User abbricht. 

**Vergleich mit menschlich geschriebenem Code:** Der von ChatGPT generiert Code ist kürzer und verwendet für die Prüfung des Spielergebnis einen klugen Loop bzw. ein simples „Else“ das mithilfe der Anzahl der gespielten Züge ein „Tie“ erkennt, wohingegen der menschlich geschrieben Code aufwendige „If“ Konstellationen innerhalb von zwei Funktionen anwendet. 
Außerdem ist der menschliche Code generell etwas komplizierter entwickelt, bezieht allerdings auch falsche/sinnlose Inputs der User mit ein, weshalb kein Szenario (im Gegensatz zum ChatGPT Code) identifiziert werden konnte, in dem der Code nicht durchläuft bzw. funktionstüchtig ist. 
Funktionierendes „Error Handling“ war uns nicht möglich mit ChatGPT zu realisieren. Zudem bietet der menschliche Code ein paar extra Features an, wie eine „Exit“ Funktion oder eine kurze Begrüßung als Einleitung zum Spiel. 
ChatGPT ist zwar in der Lage diese Feature mittels weiteren durchdachten „Prompts“ ebenso in den AI-Code zu integrieren, die tatsächliche Umsetzung bei gleichzeitigem Erhalt der Funktionalität gestaltete sich allerdings komplizierter. 

**Methoden der Code-Generierung:** Der initiale Input hat wie folgt gelautet: 

_„Write a simple tic tac toe game in python. The game should have a two player modus, it should be possible to enter a player name for each player, the game board should be displayed in the python sell, and the game outcome should be stated in the end”._

Bei anderen Formulierungen werden leicht unterschiedlich Code-Varianten generiert. Die Funktionalität bleibt aber immer erhalten. Grundsätzlich sticht aber heraus, dass die Codes bei weniger genaueren „Prompts“ nicht genau den Erwartungen entsprechen und dass je detaillierter die „Prompts“ sind, umso zieltreffender die Ergebnisse sind.  

**Dokumentation**: Mit der initialen Formulierung war der generierte Code eher spärlich kommentiert und dokumentiert.
Nach einer weiteren Anweisung bzw. „Prompt“, in der um genauere Erklärungen bzw. Dokumentierung des Codes in Form von Kommentaren gebeten wurde, ist das Endergebnis allerdings gänzlich, ausführlich und verständlich kommentiert. 

**Zusammenfassend** wurde ersichtlich, dass ChatGPT 3.5 mehr als ausreichend Coding-Fähigkeiten beherrscht, um ein simples Programm wie ein Tic-Tac-Toe Spiel ausreichend qualitativ zu entwickeln (mit Ausnahme des Error Handlings).
ChatGPT 4.0 würde mutmaßlich nochmal deutlich ausgeprägtere Fähigkeiten aufzeigen. 
