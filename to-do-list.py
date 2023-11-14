# Funktion, um eine neue Aufgabe zur Liste hinzuzufügen
def aufgabe_hinzufuegen(aufgaben_liste):
    aufgabe = input("Geben Sie die neue Aufgabe ein: ")
    aufgaben_liste.append(aufgabe)
    print("Aufgabe hinzugefügt!")

# Funktion, um eine Aufgabe von der Liste zu entfernen
def aufgabe_entfernen(aufgaben_liste):
    if aufgaben_liste:
        print("Aktuelle Aufgaben:")
        for index, aufgabe in enumerate(aufgaben_liste):
            print(f"{index + 1}: {aufgabe}")
        zu_entfernen = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie entfernen möchten: "))
        if zu_entfernen > 0 and zu_entfernen <= len(aufgaben_liste):
            del aufgaben_liste[zu_entfernen - 1]
            print("Aufgabe entfernt!")
        else:
            print("Ungültige Auswahl!")
    else:
        print("Keine Aufgaben vorhanden!")

# Funktion, um die aktuellen Aufgaben anzuzeigen
def aufgaben_anzeigen(aufgaben_liste):
    if aufgaben_liste:
        print("Aktuelle Aufgaben:")
        for index, aufgabe in enumerate(aufgaben_liste):
            print(f"{index + 1}: {aufgabe}")
    else:
        print("Keine Aufgaben vorhanden!")

# Hauptprogramm
todo_liste = []

while True:
    print("\nWas möchten Sie tun?")
    print("1: Neue Aufgabe hinzufügen")
    print("2: Aufgabe entfernen")
    print("3: Aufgaben anzeigen")
    print("4: Beenden")

    auswahl = input("Geben Sie die Nummer Ihrer Auswahl ein: ")

    if auswahl == "1":
        aufgabe_hinzufuegen(todo_liste)
    elif auswahl == "2":
        aufgabe_entfernen(todo_liste)
    elif auswahl == "3":
        aufgaben_anzeigen(todo_liste)
    elif auswahl == "4":
        break
    else:
        print("Ungültige Auswahl! Bitte wählen Sie erneut.")