'''
In diesem Modul wird die Abfrage des Admin Passwortes anhand eine GUI abgefragt.
Nach Eingabe des Passwortes kann der User auswählen ob dieser einen neuen Account
anlegen oder einen Account löschen möchte.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import messagebox
# Methode aus Pictures.py aufrufen, um Bild aus Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Funktionsaufruf von anderem Modul um dessen GUI zu öffnen
from Menu_create_account import menu_account_create
from Menu_delete_account import menu_account_delete


# Funktion: Erstellung der GUI
def menu_admin(parent_root):
    # GUI-Fenster herstellen
    global GUI_menu
    GUI_menu = tk.Toplevel()
    # GUI Fenstergröße
    GUI_menu.geometry("450x430")
    # GUI Fenstertitel
    GUI_menu.title("Menü Account anlegen/löschen")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text= "Account anlegen oder löschen", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(340, 320))

    # Frame: Erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=390, height=120, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=70)

    # Label: Überschrift Accountname
    headline_admin_name = tk.Label(GUI_menu, text="Admin Passwort eingeben:", bg="lightgray", font=('arial', 16))
    headline_admin_name.place(x=50, y=90)

    # Combobox: für die Eingabe oder Auswahl
    # Variable Globalisieren
    global entry_admin_pw
    # Combobox: Account
    entry_admin_pw = tk.Entry(GUI_menu, show='*', font=('arial', 13))
    # Den Cursor setzten, damit Eingaben direkt getätigt werden können.
    entry_admin_pw.focus()
    # Dropdown Eigenschaften
    entry_admin_pw.place(x=50, y=140, width=350, height=30)

    # Button: Menü Account erstellen aufrufen
    button_create = tk.Button(GUI_menu, text="Anlegen", background="green", fg="white", height=2, width=15,
            font=('arial', 12, 'bold'), command=check_pw_create)
    button_create.place(x=30, y=220)

    # Button: Menü Account löschen aufrufen
    button_delete = tk.Button(GUI_menu, text="Löschen", background="orange", fg="black", height=2, width=15,
            font=('arial', 12, 'bold'), command=check_pw_delete)
    button_delete.place(x=260, y=220)

    # Funktion: Schließt die GUI und öffnet die vorherige GUI
    def close_open_gui():
        # GUI schließen
        GUI_menu.destroy()
        # Ruft die vorherige GUI wieder auf
        parent_root.deiconify()
    # Überschreibt die Fensterleiste "x" Schließfunktion als close_open_gui()
    GUI_menu.protocol("WM_DELETE_WINDOW", close_open_gui)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2, width=15,
            font=('arial', 12, 'bold'), command=close_open_gui)
    button_close.place(x=30, y=330)

    # Aufruf der Menü GUI
    GUI_menu.mainloop()


# Funktion: Prüft die Passworteingabe des Users um in das Menü zur Account anlegen zu gelangen
def check_pw_create():
    # Eingabe in Variable speichern
    pw = entry_admin_pw.get()
    # Prüfen ob Eingabe gemacht wurde
    if pw == "":
        # Messagebox: Wenn nichts eingegeben wurde
        messagebox.showwarning("Benachrichtigung", "Es wurden keine Eingaben gemacht!")
        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()
    # Wenn Eingabe korrekt eingegeben wurde
    elif pw == "admin":
        # Eingabefeld leeren
        entry_admin_pw.delete(0, tk.END)
        # Versteckt die aktuelle GUI
        GUI_menu.withdraw()
        # Öffnen des Menüs zur Account anlegen
        menu_account_create(GUI_menu)
    # Wenn Eingabe nicht mit Passwort übereinstimmt
    elif pw != "admin":
        # Eingabefeld leeren
        entry_admin_pw.delete(0, tk.END)
        # Messagebox: Fehlermeldung
        messagebox.showwarning("Benachrichtigung", "Das eingegebene Passwort ist falsch!")
        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()


# Funktion: Prüft die Passworteingabe des Users um in das Menü zur Account löschen zu gelangen
def check_pw_delete():
    # Eingabe in Variable speichern
    pw = entry_admin_pw.get()
    # Prüfen ob Eingabe gemacht wurde
    if pw == "":
        # Messagebox: Wenn nichts eingegeben wurde
        messagebox.showwarning("Benachrichtigung", "Es wurden keine Eingaben gemacht!")
        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()
    # Wenn Eingabe korrekt eingegeben wurde
    elif pw == "admin":
        # Eingabefeld leeren
        entry_admin_pw.delete(0, tk.END)
        # Versteckt die aktulle GUI
        GUI_menu.withdraw()
        # Öffnen des Menü zur Account Löschung
        menu_account_delete(GUI_menu)
    # Wenn Eingabe nicht mit Passwort übereinstimmt
    elif pw != "admin":
        # Eingabefeld leeren
        entry_admin_pw.delete(0, tk.END)
        # Messagebox: Wenn Passwort falsch ist
        messagebox.showwarning("Benachrichtigung", "Das eingegebene Passwort ist falsch!")
        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()
