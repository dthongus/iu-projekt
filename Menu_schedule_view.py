'''
In diesem Modul kann der User einen vorhandenen Schichtplan einsehen. Dabei kann er aus einer Datumsliste den
jeweiligen Schichtplan des zugehörigen Datums aufrufen. Der User hat des Weiteren die Möglichkeit den
Schichtplan als PDF zu erzeugen, welche auf dem Desktop abgespeichert wird. Anmerkung: Der Speicherort kann auch
durch eine Funktion als Abfrage erstellt werden. Dies wäre eine zusätzliche Implementation auf Kundewunsch.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# Importieren von System Funktionen
import os
# Import der reportlab Bibliothek für die Erstellung von PDF
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import navy, grey, white, lightsteelblue, black, red, green, orange, lightgrey
# Methode aus Pictures.py aufrufen, um Bild und Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Funktion: Erstellung der GUI
def menu_sp_view(parent_root):
    global GUI_menu
    # GUI-Fenster
    GUI_menu = tk.Toplevel()
    # GUI Fenstergröße
    GUI_menu.geometry("1030x620")
    # GUI Fenstertitel
    GUI_menu.title("Menü Schichtplan einsehen")
    # GUI Überschrift
    headline = tk.Label(GUI_menu, text="Schichtplan einsehen", font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu, IMAGE_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu, IMAGE_NAME, image_size=(80, 80), position=(920, 520))

    # Frame Schichtplan
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=590, height=370, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=60)

    # Frame Datumseingabe
    frame = tk.Frame(GUI_menu, borderwidth=1, relief="solid", bg="lightgray", width=350, height=370, padx=20, pady=20)
    frame.pack_propagate(False)
    frame.place(x=650, y=60)

    # Label: Überschrift Arbeitsplatz
    headline_workplace = tk.Label(GUI_menu, text="Arbeitsplatz", bg="lightgray", font=('arial', 16, 'bold'))
    headline_workplace.place(x=50, y=80)
    # Label: Überschrift Priorität
    headline_priority = tk.Label(GUI_menu, text="Priorität", bg="lightgray", font=('arial', 16, 'bold'))
    headline_priority.place(x=210, y=80)
    # Label: Überschrift Mitarbeiter
    headline_employee = tk.Label(GUI_menu, text="Mitarbeiter", bg="lightgray", font=('arial', 16, 'bold'))
    headline_employee.place(x=337, y=80)

    # Label: Arbeitsplätze erstellen
    workplace_1 = tk.Label(GUI_menu, text="Arbeitsplatz 1", bg="lightgray", font=('arial', 16))
    workplace_1.place(x=50, y=130)
    workplace_2 = tk.Label(GUI_menu, text="Arbeitsplatz 2", bg="lightgray", font=('arial', 16))
    workplace_2.place(x=50, y=190)
    workplace_3 = tk.Label(GUI_menu, text="Arbeitsplatz 3", bg="lightgray", font=('arial', 16))
    workplace_3.place(x=50, y=250)
    workplace_4 = tk.Label(GUI_menu, text="Arbeitsplatz 4", bg="lightgray", font=('arial', 16))
    workplace_4.place(x=50, y=310)
    workplace_5 = tk.Label(GUI_menu, text="Arbeitsplatz 5", bg="lightgray", font=('arial', 16))
    workplace_5.place(x=50, y=370)

    # Prioritäten Labels Schriftart und Größe definieren
    global label_priority_1, label_priority_2, label_priority_3, label_priority_4, label_priority_5
    label_priority_1 = tk.Label(GUI_menu)
    label_priority_2 = tk.Label(GUI_menu)
    label_priority_3 = tk.Label(GUI_menu)
    label_priority_4 = tk.Label(GUI_menu)
    label_priority_5 = tk.Label(GUI_menu)

    # Label: Mitarbeiter erstellen
    global label_employee_1, label_employee_2, label_employee_3, label_employee_4, label_employee_5
    label_employee_1 = tk.Label(GUI_menu, font=('arial', 16))
    label_employee_2 = tk.Label(GUI_menu, font=('arial', 16))
    label_employee_3 = tk.Label(GUI_menu, font=('arial', 16))
    label_employee_4 = tk.Label(GUI_menu, font=('arial', 16))
    label_employee_5 = tk.Label(GUI_menu, font=('arial', 16))

    # Label: Überschrift
    label_headline_select = tk.Label(GUI_menu, text="Bitte Datum auswählen:", anchor="w", justify="left", bg="lightgray", font=('arial', 16))
    label_headline_select.place(x=670, y=100, width=310, height=30)

    # Combobox: Eingabefeld für Datum
    global combo_date
    combo_date = ttk.Combobox(GUI_menu, justify="center", foreground="red", font=('arial', 16, 'bold'), state="readonly")
    combo_date.place(x=673, y=150, width=298, height=40)
    combo_date['values'] = datelist

    # Label: Hinweis
    label_headline_message = tk.Label(GUI_menu, text="Danach den Button aufrufen\nbetätigen.", anchor="w", justify="left", bg="lightgray", font=('arial', 16))
    label_headline_message.place(x=670, y=200, width=300, height=80)

    # Button: Schichtplan einsehen aufrufen
    button_call_sp = tk.Button(GUI_menu, text="Schichtplan aufrufen", background="blue", fg="white", height=2, width=17,
            font=('arial', 12, 'bold'), command=call_sp)
    button_call_sp.place(x=30, y=450)

    # Button: Schichtplan als PDF erzeugen aufrufen
    button_create_pdf = tk.Button(GUI_menu, text="PDF erzeugen", background="green", fg="white", height=2, width=15,
            font=('arial', 12, 'bold'), command=pdf_create)
    button_create_pdf.place(x=230, y=450)

    # Funktion: Schließt die GUI und öffnet die vorherige GUI
    def close_open_gui():
        # Aktuelle GUI schließen
        GUI_menu.destroy()
        # Ruft die vorherige GUI wieder auf
        parent_root.deiconify()

    # Überschreibt die Fensterleiste "x" Schließfunktion als close_open_gui()
    GUI_menu.protocol("WM_DELETE_WINDOW", close_open_gui)  # Überschreibt die Schließfunktion

    # Button: Schließen
    button_close = tk.Button(GUI_menu, text="Beenden", background="red", fg="black", height=2, width=15,
            font=('arial', 12, 'bold'), command=close_open_gui)
    button_close.place(x=840, y=450)

    # Aufruf der GUI
    GUI_menu.mainloop()


# Datenbank Verzeichnis holen und verbinden
db_path = database_path()
mydb = sqlite3.connect(db_path)
cursor = mydb.cursor()


# Funktion: Datumswerte aus Datenbank als Liste erstellen. Dient zur Befüllung der Combobox für User Auswahl des Datums
def date_list():
    # Spalte der Tabelle aus Datenbank bestimmen und Datum sortieren
    sql = '''
       SELECT DISTINCT Datum
       FROM Schichtpläne
       ORDER BY Datum
       '''
    cursor.execute(sql)
    dates = cursor.fetchall()
    # Doppelte Datumswerte eliminieren und nur einfach ausgeben
    unique_dates = [date[0] for date in dates]
    return unique_dates

# Mitarbeiterliste in Variable speichern, wird für die Combobox zur Befüllung benötigt
global datelist
datelist = date_list()


# Funktion: Suchen der Prioritäten und Mitarbeiter aus der Datenbank zum ausgewählten Datum
def werte_aus_db():
    # SQL Abfrage ausführen, um die Zeilen für das angegebene Datum zu erhalten
    cursor.execute("SELECT Priorität, Mitarbeiter FROM Schichtpläne WHERE Datum = ?", (date_sp,))
    db_value_list = cursor.fetchall()
    return db_value_list


# Funktion: Prioräten und Mitarbeiter zum ausgewählten Datum in die GUI einfügen
def call_sp():
    # Eingegebenes Datum in Variable speichern
    global date_sp
    date_sp = combo_date.get()
    # Funktion werte_aus_db aufrufen
    db_value_list = werte_aus_db()

    # Prüfung: Ob Datum Einträge vorhanden sind
    if len(db_value_list) > 0:
        # Wenn Datum vorhanden ist, dann die zugehörigen Werte in die jeweiligen Labels einfügen
        for i in range(min(len(db_value_list), 5)):  # Nur die ersten 5 Werte ab dem Datum holen
            priority = db_value_list[i][0]
            employee = db_value_list[i][1]

            # Labels als Liste setzten
            label_priority_list = [label_priority_1, label_priority_2, label_priority_3, label_priority_4,
                                   label_priority_5]
            label_employee_list = [label_employee_1, label_employee_2, label_employee_3, label_employee_4,
                                   label_employee_5]

            # Prüfen: Labelhintergrundfarbe nach Prioritätbedeutung setzen und in Label einfügen
            if priority == "Hoch":
                priority_label = label_priority_list[i]
                priority_label.config(text=priority, anchor="w", justify="left", bg="red", fg="black",
                                      font=('arial', 16))
            elif priority == "Mittel":
                priority_label = label_priority_list[i]
                priority_label.config(text=priority, anchor="w", justify="left", bg="orange", fg="black",
                                      font=('arial', 16))
            elif priority == "Niedrig":
                priority_label = label_priority_list[i]
                priority_label.config(text=priority, anchor="w", justify="left", bg="green", fg="white",
                                      font=('arial', 16))

            # Positionierung der Labels
            priority_label.place(x=210, y=130 + i * 60, width=85, height=30)

            # Mitarbeiter in Label einfügen
            employee_label = label_employee_list[i]
            employee_label.config(text=employee, anchor="w", justify="left", bg="gainsboro")
            employee_label.place(x=340, y=130 + i * 60, width=200, height=30)


# Funktion: Schichtplan als PDF erzeugen
def pdf_create():
    try:
        # Priorität in Objekte speichern
        priority_1 = label_priority_1.cget("text")
        priority_2 = label_priority_2.cget("text")
        priority_3 = label_priority_3.cget("text")
        priority_4 = label_priority_4.cget("text")
        priority_5 = label_priority_5.cget("text")
        # Mitarbeiter Daten holen
        employee_1 = label_employee_1.cget("text")
        employee_2 = label_employee_2.cget("text")
        employee_3 = label_employee_3.cget("text")
        employee_4 = label_employee_4.cget("text")
        employee_5 = label_employee_5.cget("text")
        kw = str(combo_date.get())

        # Name der PDF-Datei festlegen und in Variable speichern
        filename = f"Schichtplan_{date_sp}.pdf"

        # Funktion: PDF-Eigenschaften aufrufen
        pdf_character(filename, priority_1, priority_2, priority_3, priority_4, priority_5, employee_1, employee_2,
                      employee_3, employee_4, employee_5, date_sp)

        # Messagebox: Hinweis wo die PDF-Datei gespeichert wurde
        messagebox.showinfo("Speicherort", "Der Schichtplan wurde auf dem Desktop gespeichert!")

        # GUI wieder in Vordergrund setzten
        GUI_menu.lift()
        GUI_menu.focus_force()

    except:
        # Messagebox: Fehlermeldung ausgeben, falls bereits ein Schichtplan mit dem gleichen Namen geöffnet ist
        messagebox.showerror("Fehler!","Sie müssen zuerst den geöffneten Schichtplan.pdf\nschließen, da sonst keine neue PDF erzeugt\nwerden kann!\n\nOder es wurde keine Auswahl getroffen!")


# Funktion: PDF Eigenschaften festlegen
def pdf_character(filename, priority_1, priority_2, priority_3, priority_4, priority_5, employee_1,
        employee_2, employee_3, employee_4, employee_5, date_sp):
    # Speicherort der PDF festlegen (hier Desktop)
    path_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    path_pdf = os.path.join(path_desktop, filename)
    c = canvas.Canvas(path_pdf, pagesize=landscape(letter))

    # Überschrift
    c.setFillColor(navy)
    c.rect(30, 530, 730, 40, stroke=0, fill=1)  # Position und Größe Hintergrund
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(230, 540, f"Schichtplan: {date_sp}")  # Position und Größe Schrift

    # Bereichsüberschriften
    c.setFillColor(grey)
    c.rect(30, 450, 730, 35, stroke=0, fill=1)  # Position und Größe Hintergrund
    c.setFillColor(white)
    c.setFont("Helvetica", 18)
    c.drawString(60, 460, f"Arbeitsplatz")  # Position und Größe Schrift
    c.drawString(260, 460, f"Priorität")  # Position und Größe Schrift
    c.drawString(420, 460, f"Mitarbeiter")  # Position und Größe Schrift

    # Position und Größe der Rechtecke/Bereiche
    rect_specs = [
        (30, 410, 730, 30),
        (30, 370, 730, 30),
        (30, 330, 730, 30),
        (30, 290, 730, 30),
        (30, 250, 730, 30)
    ]

    # Textinhalte
    texts = [
        ("Arbeitsplatz 1", priority_1, employee_1),
        ("Arbeitsplatz 2", priority_2, employee_2),
        ("Arbeitsplatz 3", priority_3, employee_3),
        ("Arbeitsplatz 4", priority_4, employee_4),
        ("Arbeitsplatz 5", priority_5, employee_5)
    ]

    # Erstellen der Rechtecke und Texte
    for i, (rect_x, rect_y, rect_width, rect_height) in enumerate(rect_specs):
        # Rechteck Hintergrundfarbe
        c.setFillColor(lightgrey)
        c.rect(rect_x, rect_y, rect_width, rect_height, stroke=0, fill=1)

        # Positionierung der Texte
        text1, text2, text3 = texts[i]
        text_specs = [
            (text1, rect_x + 30, rect_y + 8),
            (text2, rect_x + 230, rect_y + 8),
            (text3, rect_x + 390, rect_y + 8)
        ]

        # Größe der Schrift
        c.setFont("Helvetica", 18)

        # Abfrage um Textfarbe der Prioritäten zu ändern
        for text, text_x, text_y in text_specs:
            # Standardfarbe
            color = black
            # Bestimme die Schriftfarbe für text2 (Priorität)
            if text == text2:  # Nur Prioritäten Schriftfarbe ermitteln
                if "Hoch" in text:
                    color = red
                elif "Mittel" in text:
                    color = orange
                elif "Niedrig" in text:
                    color = green

            # Schriftfarbe festlegen
            c.setFillColor(color)
            # Erstellen der Texte
            c.drawString(text_x, text_y, text)

    # Firmenlogo in die PDF einfügen
    # Verzeichnis bestimmen
    BILD_PATH = os.path.join(os.path.dirname(__file__), 'Bilder', 'Firmen_Logo.png')
    # Bild hinzufügen, Größe und Position anpassen
    c.drawImage(BILD_PATH, 657, 40, width=100, height=95)

    # Speichern des PDFs
    c.save()
    # Öffne die PDF mit dem Standardprogramm des Nutzers/PC
    os.startfile(path_pdf)


