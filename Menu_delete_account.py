'''
In diesem Modul kann ein bestehender User Account gelöscht werden.
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
def menu_account_delete(parent_root):
    # GUI-Fenster
    global GUI_menu
    GUI_menu = tk.Toplevel()
    # GUI Fenstertitel
    GUI_menu.title("Menü Account löschen")

    # Treeview = Liste/Tabelle in der tkinter GUI
    # Den Treeview als ttk Style Objekt setzten
    treeview_look = ttk.Style()

    # Liste optisch anpassen
    treeview_look.configure("Treeview",
        background="#d3d3d3",   # Hintergrundfarbe der Liste
        foreground="black",     # Schriftfarbe
        rowheight=30,           # Abstände zwischen den Zeilen
        font=('Arial', 14)
        )

    # Überschrift optisch anpassen
    treeview_look.configure("Treeview.Heading",
        background="#004080",
        foreground="Black",
        font=('Arial', 14, 'bold')
        )

    # Hintergrundfarbe der gewählten Zeile anpassen
    treeview_look.map('Treeview',
        background=[('selected', '#0000FF')],
        foreground=[('selected', '#FFFFFF')],
        )

    # # GUI Treeview erzeugen
    treeview = ttk.Treeview(GUI_menu, columns=("User",), show='headings')
    # Treeview Überschrift
    treeview.heading("User", text="Account")
    # Treeview positionieren
    treeview.place(x=30, y=60, width=477, height=350)
    # Treeview Spalte setzen und Breite festlegen
    treeview.column('User', width=150)
    # Treeview Größe
    GUI_menu.geometry("535x590")

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(427, 500))

    # Label: Hinweistext zur Verwendung
    notice_message = tk.Label(GUI_menu, text="Bitte wählen Sie eine Account in der Liste aus und\nbestätigen Sie "
        "mit dem Bestätigen Button ", foreground="green", font=('arial', 12))
    notice_message.place(x=90, y=10)

    # Button: Ausführung der Löschfunktion
    button_execute = tk.Button(GUI_menu, text="Löschen", background="orange", fg="black", height=2, width=14,
        font=('arial', 12, 'bold'), command=lambda: delete_selection(treeview))
    button_execute.place(x=30, y=430)

    # Funktion: Schließt die GUI und öffnet die vorherige GUI
    def close_open_gui():
        # Aktuelle GUI schließen
        GUI_menu.destroy()
        # Ruft die vorherige GUI wieder auf
        parent_root.deiconify()

    # Überschreibt die Fensterleiste "x" Schließfunktion als close_open_gui()
    GUI_menu.protocol("WM_DELETE_WINDOW", close_open_gui)  # Überschreibt die Schließfunktion

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2,
        width=14, font=('arial', 12, 'bold'), command=close_open_gui)
    button_close.place(x=357, y=430)

    # Treeview anzeigen
    show_table(treeview)
    # Aufruf der Menü GUI
    GUI_menu.mainloop()


# Datenbank Verzeichnis holen und verbinden
db_path = database_path()
mydb = sqlite3.connect(db_path)
cursor = mydb.cursor()


# Funktion: Erzeugen der Namensliste für das Treeview
def show_table(tree):
    # Aktualisierung Treeview: Falls Account gelöscht wurde, dann entferne diesen aus dem Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Tabellenspalte Account aus der Datenbank wählen und die User alphabetisch sortieren
    cursor.execute("SELECT User FROM Account ORDER BY User ASC")
    # Alle Daten in der Tabelle auswählen
    rows = cursor.fetchall()

    # Befüllen des Treeview mit dem Inhalt der Datenbank
    for row in rows:
        tree.insert('', 'end', values=(row[0],))


# Funktion: Löschen des ausgewählten Accounts
def delete_selection(tree):
    # Die Auswahl als Variable speichern
    selected_item = tree.selection()
    # Prüfung: Ob ein Accountname ausgewählt wurde
    if not selected_item:
        # Messagebox: Falls kein Name gewählt wurde
        messagebox.showwarning("Benachrichtigung", "Es wurde kein Account ausgewählt!")
    # Wenn Account ausgewählt wurde, dann lösche den ausgewählten Account
    else:
        # Ausgewählter Account in Variable speichern
        item = tree.item(selected_item)
        selected = item['values'][0]

        # Messagebox: Sicherheitsfrage mit Bestätigungsaufforderung, ob der Account wirklich gelöscht werden soll
        confirm = messagebox.askyesno("Bestätigung", f"Möchten Sie den Account '{selected}' wirklich löschen?")
        # Prüfen: Wenn mit Ja bestätigt wird
        if confirm:
            # Bei Bestätigung, lösche den Account
            cursor.execute("DELETE FROM Account WHERE User = ?", (selected,))
            mydb.commit()
            messagebox.showinfo("Erfolg", f"Account '{selected}' wurde gelöscht.")
        # Wenn abgebrochen wird
        else:
            # Messagebox: Bei Abbruch
            messagebox.showinfo("Abgebrochen", f"Löschung von Account '{selected}' wurde abgebrochen.")

        # Speichern der Änderung
        mydb.commit()

        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()

        # Den Treeview wieder erneut anzeigen, damit die aktuelle Mitarbeiterliste aus der Datenbank angezeigt wird
        show_table(tree)
