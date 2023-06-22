# AI REVIEW: TO-DO-LIST

Folgendes Review analysiert die Coding Fähigkeiten von ChatGPT 3.5 für das Programmieren einer To-Do-List Web-App anhand sieben Aspekten.  Dabei wird der AI-generierte Code mit dem menschlich entwickelten verglichen. 

**Funktionalität:** Der generierte Code ist voll funktionstüchtig. ChatGPT 3.5 konnte mit einem detaillierten Prompt alle Erwartungen/Requirements gänzlich erfüllen. Auch die Database mit SQLAlchemy funktioniert ohne Probleme.

**Datentypen und Variablennamen:** Der generierte Code verwendet durchgehend sinnvolle Datentypen sowie passende Variablen.

**Übersichtlichkeit und Struktur:** Der Code ist logisch strukturiert, übersichtlich und leicht verständlich. Es werden klar benannte Funktionen in sinnvoller Reihenfolge für die notwendigen Operationen verwendet sowie Abstände integriert, die für eine klare visuelle Übersicht sorgen. 
Der AI-code verfolgt dieselbe Reihenfolge und Struktur wie der menschlich Geschriebene. 

**Effizienz:** Der Code weist keine Redundanzen auf und ist genauso effizient gestaltet wie der menschlich geschriebene. 

**Vergleich mit menschlich geschriebenem Code**: Der AI-Code unterscheidet sich erstaunlicherweise nur wenig von dem menschlich Geschriebenen. 
Abgesehen von unterschiedlichen Namen für Variablen ist der größte Unterschied, dass der AI generierte Code die „Update/Edit“ Funktion erweitert. Beim AI generierten Code ist es daher auch möglich den Namen bzw. die Beschreibung eines Tasks über die „Update/Edit“ Funktion zu ändern, wohingegen der menschlich geschriebene Code nur erlaubt den Status zu aktualisieren.  
Für die „Edit“ Funktion (Anpassen des Namens eines bereits vorhandenen Tasks) des AI-Codes hat ChatGPT auch ein eigenes html-file kreiert, das beim menschlichen Code, aufgrund der simpleren Funktionsweise, redundant gewesen wäre. 

**Methoden der Code-Generierung:** Der initiale Input hat wie folgt gelautet: 

_"Write a python code for a simple to do list web-app using the package flask.  The to do list app should incorporate the following functions: add a new task, delete a task, edit/update a task, adjust the current status of the task. There should be three possible status "Coming Up", "in Progress", and "Done". 
The visual styling should be created with Semantic UI using a template html file/code. The Tasks should be stored in a Database created with SQLAlchemy."_

Bei genauerer Betrachtung des Prompts erklärt sich, weshalb ChatGPT die „Update“ Funktion im Vergleich zum menschlichen Code erweitert hat. Die Formulierung „Edit/Update“ suggerierte der AI, dass nicht nur Status aktualisiert, sondern auch die Beschreibung des Tasks angepasst werden können soll. 
Bei anderen Formulierungen des initialen Prompts unterscheidet sich der Output nur geringfügig.

**Dokumentation**: Dokumentation und Kommentierung innerhalb des AI-Codes war nach dem ersten Prompt interessanterweise kaum vorhanden. Allerdings wurden hilfreiche Erläuterungen und Hilfestellungen im Chatfenster von ChatGPT selbst geboten. 
Nach einer weiteren Anweisung, hat ChatGPT jedoch auch innerhalb des Codes qualitative Kommentare integriert. 

**Zusammenfassend** konnte festgestellt werden, dass ChatGPT 3.5 eine simple To-Do-List Web App mit Flask inklusive Database mit SQLAlchemy qualitativ und effizient programmieren kann. ChatGPT 4.0 würde mutmaßlich nochmal deutlich ausgeprägtere Fähigkeiten aufzeigen.
