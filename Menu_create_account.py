'''
In diesem Modul kann ein neuer User Account für das Login angelegt werden.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Funktion: Erstellung der GUI
def menu_account_create(parent_root):
    # GUI-Fenster herstellen
    global GUI_menu
    GUI_menu = tk.Toplevel()
    # GUI Fenstergröße
    GUI_menu.geometry("540x515")
    # GUI Fenstertitel
    GUI_menu.title("Menü Account hinzufügen")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text= "Account hinzufügen", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(430, 418))

    # Frame erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=480, height=240, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=70)

    # Label: Überschrift Accountname
    headline_account = tk.Label(GUI_menu, text="Accountname:", bg="lightgray", font=('arial', 16, 'bold'))
    headline_account.place(x=50, y=90)
    # Label: Überschrift Passwort vergabe
    headline_password = tk.Label(GUI_menu, text="Passwort:", bg="lightgray", font=('arial', 16, 'bold'))
    headline_password.place(x=50, y=170)
    # Label: Überschrift Zuweisung
    headline_allocate = tk.Label(GUI_menu, text="Zuweisung", bg="lightgray", font=('arial', 16, 'bold'))
    headline_allocate.place(x=50, y=250)

    # Entrys und Combobox: für die Eingabe oder Auswahl
    # Variable Globalisieren
    global entry_account
    global entry_password
    global combobox_allocate

    # Entry: Account
    entry_account = tk.Entry(GUI_menu, font=('arial', 13))
    # Den Cursor setzten, damit Eingaben direkt getätigt werden können.
    entry_account.focus()
    # Dropdown Eigenschaften
    entry_account.place(x=230, y=90, width=250, height=30)

    # Entry: Passwort
    entry_password = tk.Entry(GUI_menu, show='*', font=('arial', 13))
    entry_password.place(x=230, y=170, width=250, height=30)

    # Combobox: Zuweisung
    combobox_allocate = ttk.Combobox(GUI_menu, values=["Führungsebene", "Planerebene"], state="readonly",
        font=('arial', 13))
    combobox_allocate.set("")
    combobox_allocate.place(x=230, y=250, width=250, height=30)

    # Button: Speichern ausführen
    button_save = tk.Button(GUI_menu, text="Anlegen", background="blue", fg="white", height=2, width=15,
            font=('arial', 12, 'bold'), command=save)
    button_save.place(x=30, y=350)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2, width=15,
            font=('arial', 12, 'bold'), command=GUI_menu.destroy)
    button_close.place(x=350, y=350)

    # Aufruf der Menü GUI
    GUI_menu.mainloop()


# Datenbank Verzeichnis holen und verbinden
db_path = database_path()
mydb = sqlite3.connect(db_path)
cursor = mydb.cursor()


# Funktion: Speichern des Mitarbeiters in die Datenbank
def save():
    # Prüfung: Sind alle Eingaben und Auswahl getätigt?
    if combobox_allocate.get() == "" or entry_account.get() =="" or entry_password.get() == "":
        # Messagebox: Falls nicht alle Eingaben und Auswahl getätigt wurden
        messagebox.showerror("Fehler", "Eingabefelder dürfen nicht leer sein und "
            "ein Zuweisung gewählt werden!")
        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()
    # Falls der User alle Eingaben gemacht und die Zuweisung ausgewählt hat, dann führe den folgenden Code aus
    else:
        # Priorität aus Schichtplan in Variable speichern
        value_account = entry_account.get()
        # Mitarbeiter aus Schichtplan in Variable speichern
        value_password = entry_password.get()
        # Mitarbeiter aus Schichtplan in Variable speichern
        value_allocate = combobox_allocate.get()

        # Suche den eingegebenen Namen ob dieser in der Datenbank vorhanden ist
        cursor.execute('SELECT User FROM Account WHERE User = ?', (value_account,))
        result = cursor.fetchone()

        # Prüfung: Ist der Name bereits in der Datenbank vorhanden?
        if result:
            # Messagebox: Meldung das der Name bereits in der Datenbank vorhanden ist
            messagebox.showwarning("Benachrichtigung", "Account bereits vorhanden!")
            # GUI wieder in Vordergrund setzten
            GUI_menu.lift()
            GUI_menu.focus_force()
        # Falls nicht vorhanden, dann speichere die Eingaben in die Datenbank
        else:
            # Daten in Liste packen
            save_data = [
                (value_account, value_password, value_allocate)
            ]

            # Einträge in die Datenbank speichern
            cursor.executemany('''INSERT INTO Account (User, Passwort, Account) VALUES (?, ?, ?)''',
                save_data)

            # Änderungen in Datenbank speichern
            mydb.commit()
            # GUI schließen
            GUI_menu.destroy()
            # Messagebox: Bestätigung der Speicherung
            message_text = f"Account: {value_account} wurde erfolgreich angelegt!"
            messagebox.showinfo( "Meldung: ",  message_text)
