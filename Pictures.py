'''
In diesem Modul werden die Firmenlogos und Icon definiert. Es werden die Verzeichnisse initialisiert und Bilder
angepasst. Andere Funktionen können sich die Instanzen aus diesem Modul/Klasse entnehmen. Somit ist
diesbezüglich eine einfachere Wartbarkeit und eine bessere Übersichtlichkeit des Skripts gegeben.
'''


# Import des tkinter Framework zur Visualisierung
import tkinter as tk
# Import von Pillow Bibliothek zu Erstellung von Bildern
from PIL import Image, ImageTk
# Importieren von System Funktionen
import os
# Importieren von Funktionen für die Verwendung von Variablen
import sys


# Dateinamen angeben
IMAGE_NAME = "Firmen_Logo.png"
ICON_NAME = "Icon.ico"

# Unterordner Namen angeben
IMAGE_FOLDER = "Bilder"

# Klasse mit Methoden
class PictureLoader:
    # Methode: Konstruktor erzeugen, welche aber keine Funktion beinhaltet, dient als Platzhalter für ander
    # Funktionen/Methoden die später aufgerufen werden
    def __init__(self):
        pass

    # Methode: Verzeichnis festlegen
    def get_resource_path(self, relative_path):
        # Verzeichnisangabe MEIPASS welches von PyInstaller als temporäres Verzeichnis für die Bilder verwendet
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # Methode: Vollständiges Verzeichnis der Bilddatei
    def get_image_path(self, image_name):
        return self.get_resource_path(os.path.join(IMAGE_FOLDER, image_name))

    # Methode:  Bild laden
    def load_image(self, image_name):
        image_path = self.get_image_path(image_name)
        # print(f"Bildpfad (load_image): {image_path}") --> nur zur Prüfung, ob das Verzeichnis passt, nach Bedarf.
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        return photo

    # Methode: Eigenschaften der Bilddatei und Einfügen in einem tkinter Label
    def display_image(self, root, image_name, image_size, position):
        image_path = self.get_image_path(image_name)
        # print(f"Bildpfad (display_image): {image_path}")
        image = Image.open(image_path)
        image = image.resize(image_size, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Bild in Label integrieren
        label = tk.Label(root, image=photo)
        # Referenz fixieren, um Python Garbage Collection zu vermeiden
        label.image = photo
        # Bild positionieren
        label.place(x=position[0], y=position[1])

    # Fenstericon erstellen und einfügen
    def set_window_icon(self, root, icon_name):
        if icon_name:
            icon_path = self.get_image_path(icon_name)
            # print(f"Iconpfad: {icon_path}")
            # Prüfung: Ob Verzeichnis korrekt ist
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
