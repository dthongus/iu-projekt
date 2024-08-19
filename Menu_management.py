'''
In diesem Modul wird die GUI der Führungsebene angezeigt. Hier kann der User die Prioritäten zu den einzelnen
Arbeitsplätzen festlegen. Zudem kann der User von hier aus in das Menü zum Einsehen der vorhandenen Schichtpläne
gelangen.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Funktionsaufruf von anderem Modul um dessen GUI zu öffnen
from Menu_schedule_view import  menu_sp_view
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Funktion: Erstellung der GUI
def menu_management():
    # GUI-Fenster herstellen
    global GUI_menu
    GUI_menu = tk.Tk()
    # GUI Fenstergröße
    GUI_menu.geometry("700x570")
    # GUI Fenstertitel
    GUI_menu.title("Prioritätenvergabe")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text="Prioritätenvergabe", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(590, 470))

    # Frame erstellen
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=340, height=270, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=330, y=90)

    # Label: Hinweis
    advisory1 = tk.Label(frame, text="Erläuterung Prioritäten:", bg="lightgray", justify="left",
                         font=('arial', 10, 'bold'))
    advisory1.place(x=0, y=0)

    # Label: Hinweis
    advisory2 = tk.Label(frame,
                         text="Hoch\nArbeitsplatz muss ständig besetzt sein,\nIm Schichtplan wird es rot angezeigt"
                              "\n\nMittel\nArbeitsplatz sollte besetzt sein wenn alle\nArbeitsplätze mit hoher "
                              "Priorität besetzt wurden.\nIm Schichtplan wird es gelb angezeigt.\n\nNiedrig\nArbeitsplatz muss nicht besetzt "
                              "sein.\nIm Schichtplan wird dies grün angezeigt.", bg="lightgray", justify="left",
                         font=('arial', 10))
    advisory2.place(x=0, y=30)

    # Label: Arbeitsplatz 1
    workplace_1 = tk.Label(GUI_menu, text="Arbeitsplatz 1", font=('arial', 16))
    workplace_1.place(x=30, y=90)
    # Label: Arbeitsplatz 2
    workplace_2 = tk.Label(GUI_menu, text="Arbeitsplatz 2", font=('arial', 16))
    workplace_2.place(x=30, y=150)
    # Label: Arbeitsplatz 3
    workplace_3 = tk.Label(GUI_menu, text="Arbeitsplatz 3", font=('arial', 16))
    workplace_3.place(x=30, y=210)
    # Label: Arbeitsplatz 4
    workplace_4 = tk.Label(GUI_menu, text="Arbeitsplatz 4", font=('arial', 16))
    workplace_4.place(x=30, y=270)
    # Label: Arbeitsplatz 5
    workplace_5 = tk.Label(GUI_menu, text="Arbeitsplatz 5", font=('arial', 16))
    workplace_5.place(x=30, y=330)

    # Inhalt für Dropdownliste (Combobox) mit Prioritäten festlegen.
    selectionlist = ["Hoch", "Mittel", "Niedrig"]

    # Comboboxen globalisieren für save() Funktion
    global combobox1,combobox2, combobox3, combobox4, combobox5

    # Dropdownliste: Als Combobox für Arbeitsplatz 1
    combobox1 = ttk.Combobox(GUI_menu, values=selectionlist)
    combobox1.current(0)
    # Dropdown positionieren
    combobox1.place(x=200, y=90, width=100, height=30)
    # Dropdownliste: Als Combobox für Arbeitsplatz 2
    combobox2 = ttk.Combobox(GUI_menu, values=selectionlist)
    combobox2.current(0)
    combobox2.place(x=200, y=150, width=100, height=30)
    # Dropdownliste: Als Combobox für Arbeitsplatz 3
    combobox3 = ttk.Combobox(GUI_menu, values=selectionlist)
    combobox3.current(0)
    combobox3.place(x=200, y=210, width=100, height=30)
    # Dropdownliste: Als Combobox für Arbeitsplatz 4
    combobox4 = ttk.Combobox(GUI_menu, values=selectionlist)
    combobox4.current(0)
    combobox4.place(x=200, y=270, width=100, height=30)
    # Dropdownliste: Als Combobox für Arbeitsplatz 5
    combobox5 = ttk.Combobox(GUI_menu, values=selectionlist)
    combobox5.current(0)
    combobox5.place(x=200, y=330, width=100, height=30)

    # Button: Ausführung der Speicherung
    button_save = tk.Button(GUI_menu, text="Übernehmen", background="blue", fg="white", height=2, width=15,
                               font=('arial', 12, 'bold'), command=save)
    button_save.place(x=30, y=400)

    # Button: Menü Schichtpläne einsehen aufrufen
    button_show_sp = tk.Button(GUI_menu, text="Schichtplan einsehen", background="green",
        fg="white", height=2, width=18, font=('arial', 12, 'bold'), command=view_schedule)
    button_show_sp.place(x=230, y=400)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2, width=15,
        font=('arial', 12, 'bold'), command=GUI_menu.destroy)
    button_close.place(x=510, y=400)

    # Aufruf der GUI
    GUI_menu.mainloop()


# Funktion: Aufruf Schichtplan einsehen
def view_schedule():
    # Aktuelle GUI schließen
    GUI_menu.withdraw()
    # GUI Schichtplan einsehen aufrufen
    menu_sp_view(GUI_menu)


# Funktion: Prioritäten in die Datenbank speichern
def save():
    # Werte aus den Comboboxen in Variable speichern
    Priority_1 = combobox1.get()
    Priority_2 = combobox2.get()
    Priority_3 = combobox3.get()
    Priority_4 = combobox4.get()
    Priority_5 = combobox5.get()

    # Datenbank Verzeichnis holen und verbinden
    db_path = database_path()
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    # Alte Werte in der Tabelle löschen
    cursor.execute('DELETE FROM Prioliste')

    # Prioritäten als Liste in Variable speichern
    prio_list = [
        (Priority_1,),
        (Priority_2,),
        (Priority_3,),
        (Priority_4,),
        (Priority_5,)
    ]

    # Prioritäten in die Datenbank speichern
    cursor.executemany('INSERT INTO Prioliste (Priorität) VALUES (?)', prio_list)

    # Änderungen speichern
    mydb.commit()
    # Verbindung zur Datenbank schließen
    mydb.close()

    # Messagebox: Bestätigung der erfolgreichen Speicherung
    messagebox.showinfo("Benachrichtigung", "Prioritäten wurden gespeichert!")


if __name__ == "__main__":
    menu_management()




