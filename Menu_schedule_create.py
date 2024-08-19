'''
In diesem Modul kann der User einen Schichtplan erstellen. Dabei wird dem User die Prioritäten farblich zu
den jeweiligen Arbeitsplatz angezeigt, welche durch die Führungsebene vorab getroffen wurden.
Zudem hat der User die Möglichkeit aus dem Schichtplan eine PDF zu erzeugen, welche auf dem Desktop abgelegt wird.
Bei der Erzeugung, wird die PDF von jeweiligen PDF viewer des Systems/Users geöffnet. Es sind zusätzlich noch einige
Hinweistexte zur Funktionalität hinterlegt. Anmerkung: Der Speicherort kann auch durch eine Funktion als Abfrage
erstellt werden. Dies wäre eine zusätzliche Implementation auf Kundewunsch.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Import der Sqlite Bibliothek für die Datenbank
import sqlite3
# System Funktionen importieren
import os
# Import der reportlab Bibliothek für die Erstellung von PDF
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import navy, grey, white, lightsteelblue, black, red, green, orange, lightgrey
# Import datetime für das aktuelle Datum
from datetime import datetime
# Methode aufrufen um Bild aus Logo zu holen
from Pictures import PictureLoader, IMAGE_NAME, ICON_NAME
# Importieren der Funktion zur Verzeichnisangabe der Datenbank
from Database_path import database_path


# Datum in Variable speichern und Datumsformat anpassen, dient zur Anzeige im Schichtplan und Zuordnung des
# erstellten Schichtplans in der Datenbank
original_date_str = "2024-08-13"
original_format = "%Y-%m-%d"
date = datetime.strptime(original_date_str, original_format)
new_format = "%d.%m.%Y"
datetime = date.strftime(new_format)


# Funktion: Erstellung der GUI
def menu_sp_create(parent_root):
    # GUI-Fenster herstellen
    global GUI_menu_create
    GUI_menu_create = tk.Toplevel()
    # GUI Fenstergröße
    GUI_menu_create.geometry("870x640")
    # GUI Fenstertitel
    GUI_menu_create.title("Menü Schichtplan erstellen")
    # GUI Überschrift
    text = "Schichtplan für den "
    headline = tk.Label(GUI_menu_create, text= text + str(datetime), font=('arial', 18, 'bold'))
    headline.place(x=30, y=15)

    # Icon und Bild laden
    picture_loader = PictureLoader()
    # Fenster-Icon in GUI einfügen
    picture_loader.set_window_icon(GUI_menu_create, ICON_NAME)
    # Firmenlogo in GUI einfügen und Größe anpassen sowie positionieren
    picture_loader.display_image(GUI_menu_create, IMAGE_NAME, image_size=(80, 80), position=(760, 540))

    # Frame erstellen
    frame = tk.Frame(GUI_menu_create, borderwidth=1, relief="solid", bg="lightgray", width=590,
        height=370, padx=20, pady=20)
    # Automatische Skalierung des Frames verhindern
    frame.pack_propagate(False)
    # Frame positionieren
    frame.place(x=30, y=70)

    # Label: Überschrift Arbeitsplatz
    headline_workplace = tk.Label(GUI_menu_create, text="Arbeitsplatz", bg="lightgray", font=('arial', 16, 'bold'))
    headline_workplace.place(x=50, y=90)
    # Label: Überschrift Priorität
    headline_priority = tk.Label(GUI_menu_create, text="Priorität", bg="lightgray", font=('arial', 16, 'bold'))
    headline_priority.place(x=210, y=90)
    # Label: Überschrift Mitarbeiter
    headline_employee = tk.Label(GUI_menu_create, text="Mitarbeiter", bg="lightgray", font=('arial', 16, 'bold'))
    headline_employee.place(x=337, y=90)

    # Label: Arbeitsplatz 1
    workplace_1 = tk.Label(GUI_menu_create, text="Arbeitsplatz 1", bg="lightgray", font=('arial', 16))
    workplace_1.place(x=50, y=140)
    # Label: Arbeitsplatz 2
    workplace_2 = tk.Label(GUI_menu_create, text="Arbeitsplatz 2", bg="lightgray", font=('arial', 16))
    workplace_2.place(x=50, y=200)
    # Label: Arbeitsplatz 3
    workplace_3 = tk.Label(GUI_menu_create, text="Arbeitsplatz 3", bg="lightgray", font=('arial', 16))
    workplace_3.place(x=50, y=260)
    # Label: Arbeitsplatz 4
    workplace_4 = tk.Label(GUI_menu_create, text="Arbeitsplatz 4", bg="lightgray", font=('arial', 16))
    workplace_4.place(x=50, y=320)
    # Label: Arbeitsplatz 5
    workplace_5 = tk.Label(GUI_menu_create, text="Arbeitsplatz 5", bg="lightgray", font=('arial', 16))
    workplace_5.place(x=50, y=380)

    # Label: für Prioritäten erstellen
    # Variable Globalisieren
    global label_priority_1, label_priority_2, label_priority_3, label_priority_4, label_priority_5
    # Label: Arbeitsplatz 1
    label_priority_1 = tk.Label(GUI_menu_create, justify="left", font=('arial', 16))
    label_priority_1.place(x=210, y=140, width=100, height=30)
    # Label: Arbeitsplatz 2
    label_priority_2 = tk.Label(GUI_menu_create, justify="left", font=('arial', 16))
    label_priority_2.place(x=210, y=200, width=100, height=30)
    # Label: Arbeitsplatz 3
    label_priority_3 = tk.Label(GUI_menu_create, justify="left", font=('arial', 16))
    label_priority_3.place(x=210, y=260, width=100, height=30)
    # Label: Arbeitsplatz 4
    label_priority_4 = tk.Label(GUI_menu_create, justify="left", font=('arial', 16))
    label_priority_4.place(x=210, y=320, width=100, height=30)
    # Label: Arbeitsplatz 5
    label_priority_5 = tk.Label(GUI_menu_create, justify="left", font=('arial', 16))
    label_priority_5.place(x=210, y=380, width=100, height=30)

    # Combobox: für die Eingabe oder Auswahl des Mitarbeiters
    # Variable Globalisieren
    global combobox_1, combobox_2, combobox_3, combobox_4, combobox_5
    # Combobox: Mitarbeiterliste für Arbeitsplatz 1
    combobox_1 = ttk.Combobox(GUI_menu_create, values=[], font=('arial', 13))
    # Dropdown Eigenschaften
    combobox_1.place(x=340, y=140, width=250, height=30)
    # Combobox mit Mitarbeiterliste aus der Datenbank füllen
    combobox_1.bind("<Button-1>", lambda event: employeelist())
    # Combobox: Mitarbeiterliste für Arbeitsplatz 2
    combobox_2 = ttk.Combobox(GUI_menu_create, values=[], font=('arial', 13))
    combobox_2.set("")
    combobox_2.place(x=340, y=200, width=250, height=30)
    combobox_2.bind("<Button-1>", lambda event: employeelist())
    # Combobox: Mitarbeiterliste für Arbeitsplatz 3
    combobox_3 = ttk.Combobox(GUI_menu_create, values=[], font=('arial', 13))
    combobox_3.set("")
    combobox_3.place(x=340, y=260, width=250, height=30)
    combobox_3.bind("<Button-1>", lambda event: employeelist())
    # Combobox: Mitarbeiterliste für Arbeitsplatz 4
    combobox_4 = ttk.Combobox(GUI_menu_create, values=[], font=('arial', 13))
    combobox_4.set("")
    combobox_4.place(x=340, y=320, width=250, height=30)
    combobox_4.bind("<Button-1>", lambda event: employeelist())
    # Combobox: Mitarbeiterliste für Arbeitsplatz 5
    combobox_5 = ttk.Combobox(GUI_menu_create, values=[], font=('arial', 13))
    combobox_5.set("")
    combobox_5.place(x=340, y=380, width=250, height=30)
    combobox_5.bind("<Button-1>", lambda event: employeelist())

    # Button: Speichern des Schichtplans in die Datenbank ausführen
    button_save = tk.Button(GUI_menu_create, text="Speichern", background="blue", fg="white", height=2, width=15,
            font=('arial', 12, 'bold'), command=save_check)
    button_save.place(x=30, y=470)

    # Button: PDF erstellen ausführen
    button_pdf = tk.Button(GUI_menu_create, text="PDF erzeugen", background="green", fg="white", height=2, width=15,
            font=('arial', 12, 'bold'), command=create_pdf)
    button_pdf.place(x=230, y=470)

    # Button: Hinweistext zur Eingabe Mitarbeiterliste
    button_notice= tk.Button(GUI_menu_create, text="Hinweis\nAusfüllen der Mitarbeiter", background="grey",
        fg="white", height=3, width=17, font=('arial', 12), command=filling_note)
    button_notice.place(x=640, y=70, width=200, height=80)

    # Button: Hinweistext zur Speicherung
    button_filling_advice = tk.Button(GUI_menu_create, text="Hinweis\nSpeichern Button", background="grey",
        fg="white", height=3, width=17, font=('arial', 12), command=save_advice)
    button_filling_advice.place(x=640, y=160, width=200, height=80)

    # Button: Hinweistext zur PDF Erzeugung
    button_PDF_advice = tk.Button(GUI_menu_create, text="Hinweis\nPDF erzeugen Button", background="grey",
        fg="white", height=3, width=17, font=('arial', 12), command=pdf_advice)
    button_PDF_advice.place(x=640, y=250, width=200, height=80)

    # Funktion: Schließt die GUI und öffnet die vorherige GUI
    def close_open_gui():
        # Aktuelle GUI schließen
        GUI_menu_create.destroy()
        # Ruft die vorherige GUI wieder auf
        parent_root.deiconify()

    # Überschreibt die Fensterleiste "x" Schließfunktion als close_open_gui()
    GUI_menu_create.protocol("WM_DELETE_WINDOW", close_open_gui)  # Überschreibt die Schließfunktion

    # Button: Schließen
    button_close = tk.Button(GUI_menu_create, text="Beenden", background="red", fg="black", height=2, width=15,
            font=('arial', 12, 'bold'), command=close_open_gui)
    button_close.place(x=680, y=470)

    # Funktion: Schließt die GUI_menu_exist und öffnet die vorherige GUI
    global close_open_gui_exist
    def close_open_gui_exist():
        parent_root.deiconify()  # Zeigt die erste GUI wieder an
        return  parent_root.deiconify()

    # Funktion: Prioritäten aus der Datenbank holen
    data_fetch()

    # Aufruf der Menü GUI
    GUI_menu_create.mainloop()


# Datenbank Verzeichnis holen und verbinden
db_path = database_path()
mydb = sqlite3.connect(db_path)
cursor = mydb.cursor()


# Funktion: Personalliste aus Datenbank als Liste erstellen und in die Comboboxen einfügen
def employeelist():
    # Daten aus Tabelle holen und alphabetisch sortieren
    cursor.execute("SELECT Mitarbeiter FROM Personalliste ORDER BY Mitarbeiter ASC")
    # Alle Daten in Objekt speichern
    dates = cursor.fetchall()

    # Daten zu einer Liste umwandeln
    values = [row[0] for row in dates]

    # Befüllen der Comboboxen
    combobox_1['values'] = values
    combobox_2['values'] = values
    combobox_3['values'] = values
    combobox_4['values'] = values
    combobox_5['values'] = values


# Funktion: Abrufen der Prioritäten aus der Datenbank und in Label einsetzten
def data_fetch():
    # Datenbank Cursor Objekten zuweisen
    cursor1 = mydb.cursor()
    cursor2 = mydb.cursor()
    cursor3 = mydb.cursor()
    cursor4 = mydb.cursor()
    cursor5 = mydb.cursor()

    # Die Werte aus den Spalten und Zeilen in den vorgesehenen Label einfügen.
    # LIMIT = Zeilenmenge und deren Werte / OFFSET = überspringen der Zeile
    cursor1.execute('SELECT * FROM Prioliste LIMIT 1')
    # Cursor auf den Wert richten
    prio1 = cursor1.fetchone()
    # Wert in Label als Text einfügen
    label_priority_1.config(text=str(prio1[0]))
    # Abfrage der Prioritäten für die Anpassung der Hintergrundfarbe nach Bedeutung
    content_1 = label_priority_1.cget("text")
    if content_1 == "Hoch":
        label_priority_1.config(bg="red", fg="black")
    if content_1 == "Mittel":
        label_priority_1.config(bg="orange", fg="black")
    if content_1 == "Niedrig":
        label_priority_1.config(bg="green", fg="white")
    # Für Prioritäten 2
    cursor2.execute('SELECT * FROM Prioliste LIMIT 2 OFFSET 1')
    prio2 = cursor2.fetchone()
    label_priority_2.config(text=str(prio2[0]))
    content_2 = label_priority_2.cget("text")
    if content_2 == "Hoch":
        label_priority_2.config(bg="red", fg="black")
    if content_2 == "Mittel":
        label_priority_2.config(bg="orange", fg="black")
    if content_2 == "Niedrig":
        label_priority_2.config(bg="green", fg="white")
    # Für Prioritäten 3
    cursor3.execute('SELECT * FROM Prioliste LIMIT 3 OFFSET 2')
    prio3 = cursor3.fetchone()
    label_priority_3.config(text=str(prio3[0]))
    content_3 = label_priority_3.cget("text")
    if content_3 == "Hoch":
        label_priority_3.config(bg="red", fg="black")
    if content_3 == "Mittel":
        label_priority_3.config(bg="orange", fg="black")
    if content_3 == "Niedrig":
        label_priority_3.config(bg="green", fg="white")
    # Für Prioritäten 4
    cursor4.execute('SELECT * FROM Prioliste LIMIT 4 OFFSET 3')
    prio4 = cursor4.fetchone()
    label_priority_4.config(text=str(prio4[0]))
    content_4 = label_priority_4.cget("text")
    if content_4 == "Hoch":
        label_priority_4.config(bg="red", fg="black")
    if content_4 == "Mittel":
        label_priority_4.config(bg="orange", fg="black")
    if content_4 == "Niedrig":
        label_priority_4.config(bg="green", fg="white")
    # Für Prioritäten 5
    cursor5.execute('SELECT * FROM Prioliste LIMIT 5 OFFSET 4')
    prio5 = cursor5.fetchone()
    label_priority_5.config(text=str(prio5[0]))
    content_5 = label_priority_5.cget("text")
    if content_5 == "Hoch":
        label_priority_5.config(bg="red", fg="black")
    if content_5 == "Mittel":
        label_priority_5.config(bg="orange", fg="black")
    if content_5 == "Niedrig":
        label_priority_5.config(bg="green", fg="white")

    # Rückgabe der Werte
    return prio1, prio2, prio3, prio4, prio5


# Funktion: Prioritätendaten und Mitarbetierdaten holen, damit andere Funktion darauf zugreifen können
def get_prio_employee():
    # Priorität aus Schichtplan in Varibale speichern
    global priority_1, priority_2, priority_3, priority_4, priority_5
    priority_1 = label_priority_1.cget("text")
    priority_2 = label_priority_2.cget("text")
    priority_3 = label_priority_3.cget("text")
    priority_4 = label_priority_4.cget("text")
    priority_5 = label_priority_5.cget("text")

    # Mitarbeiter aus Schichtplan in Varibale speichern
    global employee_1,employee_2, employee_3, employee_4, employee_5
    employee_1 = combobox_1.get()
    employee_2 = combobox_2.get()
    employee_3 = combobox_3.get()
    employee_4 = combobox_4.get()
    employee_5 = combobox_5.get()


# Funktion: Prüfen ob Schichtplan zum Datum bereits in der Datenbank vorhanden ist
def save_check():
    # Datenbank Abfrage, wo Werte mit dem Datum übereinstimmen
    cursor.execute(f'SELECT COUNT(*) FROM Schichtpläne WHERE Datum = ?', (datetime,))
    datalist = cursor.fetchone()[0]

    # Falls ein Schichtplan zum Datum bereits vorhanden ist, dann gib Auswahlmöglichkeiten anhand einer neuen GUI
    if datalist > 0:
        # GUI-Fenster erzeugen: Auswahlmenü mit Warnhinweis
        global GUI_menu_exist
        GUI_menu_exist = tk.Toplevel()
        # GUI Fenstergröße
        GUI_menu_exist.geometry("700x450")
        # GUI Fenstertitel
        GUI_menu_exist.title("Bestätigung")
        # GUI Überschrift
        headline_exist = tk.Label(GUI_menu_exist, text="Warnung", font=('arial', 18, 'bold underline'))
        headline_exist.place(x=30, y=15)
        # Label: Textnachricht
        headline_message = tk.Label(GUI_menu_exist, text="Es ist bereits ein Schichtplan zum Datum vorhanden!",
            fg="red", font=('arial', 18, 'bold'))
        headline_message.place(x=30, y=80)
        # Label: Auswahl Überschrift Ersetzten/Überschreiben der alten Daten
        message_replace = tk.Label(GUI_menu_exist, text="Schichtplan ersetzen:",
            font=('arial', 14, 'bold'))
        message_replace.place(x=30, y=160)
        # Label: Auswahl Überschrift: Abbrechen
        message_dont_replace = tk.Label(GUI_menu_exist, text="Keine Änderung vornehmen:",
            font=('arial', 14, 'bold'))
        message_dont_replace.place(x=30, y=300)

        # Seperator: Trennlinie in der GUI
        seperator = ttk.Separator(GUI_menu_exist, orient='horizontal')
        seperator.place(relx=0, rely=0.55, relwidth=1, relheight=0)

        # Button: Alte Schichtplan gegen neues ersetzten aufrufen
        button_execute = tk.Button(GUI_menu_exist, text="Übernehmen", background="green",
            fg="black", height=2, width=14, font=('arial', 12, 'bold'), command=replace)
        button_execute.place(x=430, y=150)

        # Funktion: Schließen der aktuellen GUI
        def close_gui_exist():
            GUI_menu_exist.destroy()

        # Button: Schließen
        button_close = tk.Button(GUI_menu_exist, text="Abbrechen", background="red",
            fg="black", height=2, width=14, font=('arial', 12, 'bold'), command=close_gui_exist)
        button_close.place(x=430, y=285)

        return
    # Falls kein Schichtplan zur Kalenderwoche existiert, dann speichere die Eingaben in die Datenbank
    else:
        # Funktion Speichern aufrufen
        save()


# Funktion: Speichern der Schichtplan Einträge in die Datenbank
def save():
    # Prioritäten und Mitarbeiter Daten initialisieren
    get_prio_employee()

    # Datum, Prioritäten und Mitarbeiter aus Schichtplan als Liste in Objekt speichern
    save_data = [
        (datetime, priority_1, employee_1),
        (datetime, priority_2, employee_2),
        (datetime, priority_3, employee_3),
        (datetime, priority_4, employee_4),
        (datetime, priority_5, employee_5)
    ]

    # Schichtplan Einträge in die Datenbank speichern
    cursor.executemany('''INSERT INTO Schichtpläne (Datum, Priorität, Mitarbeiter) VALUES (?, ?, ?)''',
        save_data)

    # Änderungen in Datenbank speichern
    mydb.commit()

    # Aktuelle GUI schließen
    GUI_menu_create.destroy()
    # Messagebox: Bestätigung der Speicherung
    messagebox.showwarning("Benachrichtigung", "Schichtplan wurde erfolgreich gespeichert!")


# Funktion: Überschreiben des vorhandenen Schichtplans zum Datum
def replace():
    # Datenbank Verzeichnis holen und verbinden
    db_path = database_path()
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()
    # Prioritäten und Mitarbeiter Daten initialisieren
    get_prio_employee()

    # Datum, Prioritäten und Mitarbeiter aus Schichtplan als Liste speichern
    new_data = [
        (datetime, priority_1, employee_1),
        (datetime, priority_2, employee_2),
        (datetime, priority_3, employee_3),
        (datetime, priority_4, employee_4),
        (datetime, priority_5, employee_5)
    ]

    # Alte Schichtplan Einträge aus der Datenbank löschen
    cursor.execute('DELETE FROM Schichtpläne WHERE Datum = ?', (datetime,))

    # Neue Schichtplan Einträge in die Datenbank speichern
    cursor.executemany('''INSERT INTO Schichtpläne (Datum, Priorität, Mitarbeiter) VALUES 
        (?, ?, ?)''', new_data)

    # Änderungen in Datenbank speichern
    mydb.commit()

    # GUI Schichtplan schließen
    GUI_menu_create.destroy()
    # Aktuelle GUI schließen
    GUI_menu_exist.destroy()

    # Schließen der GUI
    close_open_gui_exist()

    # Messagebox: Bestätigung der Speicherung
    messagebox.showwarning("Benachrichtigung", "Schichtplan wurde erfolgreich gespeichert!")


# Funktion: PDF erstellen
def create_pdf():
    try:
        # Prioritäten und Mitarbeiter Daten initialisieren
        get_prio_employee()

        # Name der PDF Datei festlegen
        filename = f"Schichtplan_{datetime}.pdf"

        # Funktion: PDF Eigenschaften aufrufen
        pdf_character(filename, priority_1, priority_2, priority_3, priority_4, priority_5, employee_1, employee_2,
            employee_3, employee_4, employee_5, datetime)

        # Messagebox: Hinweis des Speicherns
        messagebox.showinfo("Speicherort", "Der Schichtplan wurde auf dem Desktop gespeichert!")

        # GUI wieder in Vordergrund setzten
        GUI_menu_create.lift()
        GUI_menu_create.focus_force()

    except:
        # Fehlermeldung ausgeben, falls ein Fehler bei der Funktion auftriit.
        # In diesem Falle tritt ein Fehler auf, wenn bereits eine PDF geöffnet ist.
        messagebox.showerror("Fehler!","Sie müssen zuerst den geöffneten Schichtplan.pdf\nschließen, "
            "da sonst keine neue PDF erzeugt\nwerden kann!")


# Funktion: PDF Eigenschaften festlegen
def pdf_character(filename, priority_1, priority_2, priority_3, priority_4, priority_5, employee_1, employee_2,
        employee_3, employee_4, employee_5, datetime):
    # Speicherort der PDF festlegen (hier Desktop)
    path_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    path_pdf = os.path.join(path_desktop, filename)
    c = canvas.Canvas(path_pdf, pagesize=landscape(letter))

    # Überschrift
    c.setFillColor(navy)
    c.rect(30, 530, 730, 40, stroke=0, fill=1)  # Position und Größe Hintergrund
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(220, 540, f"Schichtplan für den {datetime}")  # Position und Größe Schrift

    # Bereichsüberschriften
    c.setFillColor(grey)
    c.rect(30, 450, 730, 35, stroke=0, fill=1)  # Position und Größe Hintergrund
    c.setFillColor(white)
    c.setFont("Helvetica", 18)
    c.drawString(40, 460, f"Arbeitsplatz")  # Position und Größe Schrift
    c.drawString(240, 460, f"Priorität")  # Position und Größe Schrift
    c.drawString(400, 460, f"Mitarbeiter")  # Position und Größe Schrift

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


# Funktion: Hinweistext zur Verwendung der Mitarbeiter Auswahlliste
def filling_note():
    messagebox.showinfo("Hinweis","In den Eingabefeldern MITARBEITER können die Namen eingetippt "
    "oder durch die Mitarbeiterliste mit dem Pfeil ausgewählt werden.")

# Funktion: Hinweistext zur Speicherungsfunktion
def save_advice():
    messagebox.showinfo("Hinweis","Der Schichtplan wird zum "
        "aktuellen Datum gespeichert und kann jederzeit im Bereich Schichtplan einsehen aufgerufen werden.")

# Funktion: Hinweistext zur Funktion PDF Erzeugung
def pdf_advice():
    messagebox.showinfo("Hinweis","Der Schichtplan wird zu einer PDF generiert, angezeigt und auf dem Desktop abgelegt. Die geöffnete PDF kann dann im "
    "jeweiligen PDF viewer ausgedruckt werden.")

