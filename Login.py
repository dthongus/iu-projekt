'''
In diesem Modul kann sich der User per GUI einloggen. Dabei besitzt jeder User einen Accountnamen, ein Passwort
und eine Zuweisung, welche die GUI für die Führungsebene oder Planerebene aufruft.
Aus dieser GUI kann man zusätzlich noch in den Bereich neuen Account anlegen oder löschen gelangen.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import messagebox
# Funktionsaufrufe von anderen Modulen um deren GUIs zu öffnen
from Menu_management import menu_management
from Menu_planner import menu_planner
from Admin import menu_admin
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Funktion: Erstellung der GUI
def main():
    # GUI-Fenster herstellen
    global GUI_menu
    GUI_menu = tk.Tk()
    # GUI Fenstergröße
    GUI_menu.geometry("500x690")
    # GUI Fenstertitel
    GUI_menu.title("Auswahlmenü")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text="Login", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(388, 580))

    # Frame: Erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=440, height=150, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=80)

    # Label: User
    username = tk.Label(GUI_menu, text="Account eingeben:", bg="lightgray", font=('arial', 16))
    username.place(x=45, y=110)
    # Label: Passwort
    password_input = tk.Label(GUI_menu, text="Passwort eingeben:", bg="lightgray", font=('arial', 16))
    password_input.place(x=45, y=175)
    # Frame erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="white", width=440, height=190, padx=20, pady=20)
    frame.pack_propagate(False)  # Automatische Skalierung des Frames unterbinden
    frame.place(x=30, y=360)
    # Label: Hinweis
    advisory1= tk.Label(frame, text="Login Hinweis:", bg="white", justify="left", font=('arial', 10, 'bold'))
    advisory1.place(x=0, y=0)
    # Label: Hinweis
    advisory2 = tk.Label(frame, text="Führungsebene Menü\nAccount = f    ||   Passwort = 1\n\n"
        "Planer Menü\nAccount = p   ||   Passwort = 2\n\nAdmin Passwort für neuen Account anlegen/löschen =  admin", bg="white", justify="left", font=('arial', 10))
    advisory2.place(x=0, y=30)

    # Entry: User Eingabefeld
    username_input = tk.Entry(GUI_menu, background="grey", foreground="white", justify="left", font=("arial", 14),
        textvariable=int)
    # Den Cursor setzten, damit Eingaben direkt getätigt werden können.
    username_input.focus()
    username_input.place(x=255, y=102, width=200, height=35)
    # Entry: Passwort Eingabefeld
    global userpasswort_input
    userpasswort_input = tk.Entry(GUI_menu, background="grey", foreground="white", justify="left", show='*', font=("arial", 14),
        textvariable=int)
    userpasswort_input.place(x=255, y=175, width=200, height=35)

    # Funktion: Bei Bestätigung der Entertaste -> Login ausführen
    def press_enter(event):
        logindaten()
    # Funktion ausführen bei Betätigung der Entertaste
    userpasswort_input.bind("<Return>", press_enter)

    # Prüfen welcher User sich einloggen möchte und ob die Daten stimmen
    def logindaten():
        # Eingaben in Variable speichern
        username = username_input.get()
        password = userpasswort_input.get()

        # Datenbank Verzeichnis aus Database.py holen und verbinden
        db_path = database_path()
        mydb = sqlite3.connect(db_path)
        cursor = mydb.cursor()
        # SQL-Abfrage, um zu prüfen, ob der Benutzername und das Passwort existieren
        cursor.execute("SELECT Account FROM Account WHERE User = ? AND Passwort = ?", (username, password))
        result = cursor.fetchone()
        # Datenbank schließen
        mydb.close()

        # Prüfen ob Eingaben gemacht wurden
        if username == "":
            # Messagebox: Wenn nichts eingegeben wurde
            messagebox.showwarning("Benachrichtigung", "Es wurden keine Eingaben gemacht!")
            # GUI wieder in Vordergrund setzten
            GUI_menu.lift()
            GUI_menu.focus_force()
        # Wenn Eingaben getätigt wurden: Prüfen ob Account und Passwort passt
        elif result:
            # Wenn alles passt, dann die Zuweisung des Users holen und in Variable speichern
            menu_entry = result[0]
            # Wenn Zuweisung auf Planerebene ist, dann öffne das Planer Menü
            if menu_entry == "Planerebene":
                GUI_menu.destroy()
                # Funktion: Planer Menü aufrufen
                menu_planner()
            # Wenn Zuweisung auf Führungsebene ist, dann öffne das Management Menü
            elif menu_entry == "Führungsebene":
                GUI_menu.destroy()
                # Funktion: Management Menü aufrufen
                menu_management()
        # Falls Eingaben nicht in der Datenbank vorhanden sind, dann gib Fehlermeldung
        else:
            # Messagebox: Benutzername oder Passwort ist falsch
            messagebox.showerror("Fehler", "Benutzername oder Passwort ist falsch.")

    # Button: Anmeldung ausführen
    button_login = tk.Button(GUI_menu, text="Login", background="green",
        fg="white", height=4, width=30, font=('arial', 12, 'bold'), command=logindaten)
    button_login.place(x=30, y=270, width=150, height=50)

    # Button: Account anlegen/löschen
    button_account = tk.Button(GUI_menu, text="Account anlegen/löschen", background="orange", fg="black", height=2,
            width=14, font=('arial', 12, 'bold'), command=account_create_delete)
    button_account.place(x=230, y=270, width=240, height=50)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2,
            width=14, font=('arial', 12, 'bold'), command=GUI_menu.destroy)
    button_close.place(x=30, y=584, width=150, height=50)

    # Aufruf der GUI
    GUI_menu.mainloop()


# Funktion: Aufruf der Admin GUI zur Passworteingabe und Auswahl Account anlegen oder löschen
def account_create_delete():
    # Menü Account anlegen aufrufen
    menu_admin(GUI_menu)


if __name__ == "__main__":
    main()


