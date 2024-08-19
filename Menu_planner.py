'''
In diesem Modul wird die GUI der Planerebene angezeigt. Hier hat der User vier Auswahlmöglichkeiten:
1. Einen neuen Mitarbeiter in die Personalliste einfügen
2. Einen Mitarbeiter aus der Personalliste entfernen.
3. Einen neuen Schichtplan erstellen.
4. Einen vorhandenen Schichtplan einsehen.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Funktionsaufrufe von anderen Modulen um deren GUIs zu öffnen
from Menu_add_employee import menu_add_employees
from Menu_delete_employee import menu_delete_employees
from Menu_schedule_create import menu_sp_create
from Menu_schedule_view import menu_sp_view


# Funktion: Erstellung der GUI
def menu_planner():
    # GUI-Fenster
    global GUI_menu
    GUI_menu = tk.Tk()
    # GUI Fenstergröße
    GUI_menu.geometry("790x530")
    # GUI Fenstertitel
    GUI_menu.title("Auswahlmenü")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text="Auswahlmenü Planer", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(680, 435))

    # Frame erstellen
    frame_employee = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=350, height=350, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame_employee.pack_propagate(False)
    # Frame positionieren
    frame_employee.place(x=30, y=70)

    # Label: Mitarbeiter
    advisory_employee= tk.Label(frame_employee, text="Mitarbeiterliste Bearbeiten", bg="lightgray", justify="left", font=('arial', 16))
    advisory_employee.place(x=30, y=10)

    # Button: Mitarbeiter hinzufügen aufrufen
    button_add_employees = tk.Button(frame_employee, text="Mitarbeiter hinzufügen", background="green",
        fg="white", height=4, width=25, font=('arial', 12, 'bold'), command=fct_menu_add_employees)
    button_add_employees.place(x=25, y=80)

    # Button: Mitarbeiter löschen aufrufen
    button_delete = tk.Button(frame_employee, text="Mitarbeiter löschen", background="dark green",
        fg="white", height=4, width=25, font=('arial', 12, 'bold'), command=fct_menu_delete_employees)
    button_delete.place(x=25, y=210)

    # Frame für Schichtpläne
    frame_sp = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=350, height=350, padx=20, pady=20)
    frame_sp.pack_propagate(False)  # Automatische Skalierung des Frames unterbinden
    frame_sp.place(x=410, y=70)

    # Label: Schichtpläne
    advisory_sp= tk.Label(frame_sp, text="Schichtpläne", bg="lightgray", justify="left", font=('arial', 16))
    advisory_sp.place(x=90, y=10)

    # Button: Schichtplan erstellen aufrufen
    button_sp_create = tk.Button(frame_sp, text="Schichtplan erstellen", background="blue",
        fg="white", anchor='center', justify='center', height=4, width=25, font=('arial', 12, 'bold'),
        command=fct_menu_sp_create)
    button_sp_create.place(x=25, y=80)

    # Button: Schichtpläne einsehen aufrufen
    button_sp_show = tk.Button(frame_sp, text="Schichtplan einsehen", background="dark blue",
        fg="white", height=4, width=25, font=('arial', 12, 'bold'), command=fct_menu_sp_view)
    button_sp_show.place(x=25, y=210)

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2,
            width=14, font=('arial', 12, 'bold'), command=GUI_menu.destroy)
    button_close.place(x=30, y=450)

    # Aufruf der GUI
    GUI_menu.mainloop()


# Funktion: Mitarbeiter hinzufügen aufrufen
def fct_menu_add_employees():
    # Versteckt die aktuelle GUI
    GUI_menu.withdraw()
    # Aufrufe Menü
    menu_add_employees(GUI_menu)


# Funktion: Mitarbeiter löschen aufrufen
def fct_menu_delete_employees():
    # Versteckt aktuelle GUI
    GUI_menu.withdraw()
    # Aufrufe Menü
    menu_delete_employees(GUI_menu)


# Funktion: Schichtplan erstellen aufrufen
def fct_menu_sp_create():
    # Versteckt die aktuelle GUI
    GUI_menu.withdraw()
    # Aufrufe Menü
    menu_sp_create(GUI_menu)

# Funktion: Schichtplan einsehen aufrufen
def fct_menu_sp_view():
    # Versteckt die aktuelle GUI
    GUI_menu.withdraw()
    # Aufrufe Menü
    menu_sp_view(GUI_menu)


if __name__ == "__main__":
    menu_planner()

