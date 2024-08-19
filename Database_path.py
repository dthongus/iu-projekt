'''
In diesem Modul wird der Pfad der Datenbank initialisiert. Diese kann dann von anderen Funktionen aus aufgerufen werden
'''


# Importieren von System Funktionen
import os


# Funktion: Verzeichnis der Datenbank festlegen, damit andere Funktionen/Methoden darauf zugreifen können
def database_path():
    # Verzeichnis der Datenbank
    path = os.path.join(os.path.expanduser('~'), 'Desktop')
    # Verzeichnis zur SQLite-Datenbank im Ordner 'Projekt_IU' auf dem Desktop
    path_db = os.path.join(path, 'Projekt_IU', 'Database.db')
    return path_db
