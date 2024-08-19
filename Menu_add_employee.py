'''
In diesem Modul kann ein neuer Mitarbeiter in die Personalliste der Datenbank eingefügt werden.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import messagebox
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Funktion: Erstellung der GUI
def menu_add_employees(parent_root):
    # GUI-Fenster herstellen
    global GUI_menu
    GUI_menu = tk.Toplevel()
    # GUI Fenstergröße
    GUI_menu.geometry("500x430")
    # GUI Fenstertitel
    GUI_menu.title("Menü Mitarbeiter hinzufügen")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text="Neuen Mitarbeiter hinzufügen", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(390, 330))

    # Frame: Erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=440, height=150, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=80)

    # Label: Hinweis
    new_employee = tk.Label(GUI_menu, text="Name eingeben:", bg="lightgray", font=('arial', 16))
    new_employee.place(x=55, y=110)

    # Entry: Eingabefeld für Name
    global new_name
    new_name = tk.Entry(GUI_menu, background="grey", foreground="white", justify="center", font=("arial", 14),
        textvariable=int)
    # Den Cursor setzten, damit Eingaben direkt getätigt werden können.
    new_name.focus()
    new_name.place(x=55, y=150, width=390, height=35)

    # Button: Neuen Mitarbeiter einfügen ausführen
    button_add_employee = tk.Button(GUI_menu, text="Bestätigen", background="blue", fg="white", height=2, width=14,
        font=('arial', 12, 'bold'), command=add_employee)
    button_add_employee.place(x=30, y=260)

    # Funktion: Schließt die GUI und öffnet die vorherige GUI
    def close_open_gui():
        # GUI schließen
        GUI_menu.destroy()
        # Ruft die vorherige GUI wieder auf
        parent_root.deiconify()

    # Überschreibt die Fensterleiste "x" Schließfunktion zur close_open_gui()
    GUI_menu.protocol("WM_DELETE_WINDOW", close_open_gui)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2,
        width=14, font=('arial', 12, 'bold'), command=close_open_gui)
    button_close.place(x=320, y=260)

    # Aufruf der GUI
    GUI_menu.mainloop()


# Funktion: Neuen Mitarbeiter in die Personalliste der Datenbank einfügen
def add_employee():
    # Prüfung: Prüft ob Eingabe getätigt wurde, wenn nein: dann gib eine Fehlermeldung aus
    if  new_name.get().strip() == "":
        # Messagebox: Falls keine Eingaben getätigt wurden
        messagebox.showwarning("Benachrichtigung", "Es wurden keine Eingaben getätigt!")
    # Falls Eingabefeld nicht leer ist, dann führe den folgenden Code aus
    else:
        # Datenbank Verzeichnis holen und verbinden
        db_path = database_path()
        mydb = sqlite3.connect(db_path)
        cursor = mydb.cursor()

        # Eingabe des Namens aus dem Entry in Objekt speichern
        user_input = new_name.get()

        # Weitere Prüfung: Prüfe ob der Name bereits in der Datenbank vorhanden ist
        cursor.execute('SELECT Mitarbeiter FROM Personalliste WHERE Mitarbeiter = ?', (user_input,))
        result = cursor.fetchone()
        # Prüfen: Wenn Name bereist vorhanden, dann gib eine Fehlermeldung aus
        if result:
            # Messagebox: Meldung das der Name bereits in der Datenbank vorhanden ist
            messagebox.showwarning("Benachrichtigung", "Mitarbeiter bereits vorhanden!")
        # Falls der Mitarbeiter nicht in Datenbank vorhanden ist, dann speichere den Namen in die Datenbank
        else:
            # Eingegebenen Namen in Variable speichern
            employee_name = f'"{user_input}"'
            # Speichere den Namen in die Datenbank
            cursor.execute(f'INSERT INTO Personalliste VALUES({employee_name})')

            # Messagebox: Bestätigung der erfolgreichen Speicherung
            messagebox.showinfo("Hinweis", "Der neue Mitarbeiter wurde hinzugefügt!")
            # Aktuelle GUI wieder in Vordergrund setzten
            GUI_menu.lift()
            GUI_menu.focus_force()

        # Änderungen speichern
        mydb.commit()
        # Datenbank schließen
        mydb.close()

