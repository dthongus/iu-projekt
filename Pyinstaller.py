'''
Dieses Modul dient zur Erstellung einer Windows-EXE Datei. Die Funktion hat keinen Zusammenhang mit der eigentlichen
Funktionalität des Programms.
'''


'''
Ausführungsbefehl =         python pyinstaller.py Login.py Schichtplan
'''


# Dient zur Ausführung von Python Programmen/Quellcodes bei der erstellten exe Datei
import subprocess
# Importieren von System Funktionen
import os
# Importieren von Funktionen für die Verwendung von Variablen
import sys


# Funktion um Pyinstaller zu starten welche eine exe Datei erzeugt
def create_executable(script_path, output_name="output"):
    # Verzeichnis für den Projektordner und den Unterordner EXE
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des Skripts
    dist_path = os.path.join(project_dir, "EXE")  # EXE-Ordner im Projektordner

    # Stelle sicher, dass der EXE-Ordner existiert
    if not os.path.exists(dist_path):
        os.makedirs(dist_path)

    # Eigenschaften festlegen und Dateien hinzufügen
    command = [
        "pyinstaller",
        "--onefile",  # exe-Datei als eine Datei erstellen
        "--noconsole",  # Es wird das GUI ohne Console aufgerufen
        f"--icon=Bilder/Icon.ico",  # Icon Bilddatei importieren
        f"--add-data=Bilder/Firmen_Logo.png;Bilder",  # Firmenlogo Bilddatei importieren
        f"--add-data=Database.db;.",  # Datenbank hinzufügen
        f"--distpath={dist_path}",  # Ausgabeverzeichnis wo die exe-Datei gespeichert werden soll
        f"--name={output_name}",  # Name der exe-Datei
        script_path  # Das Modul auswählen, welches bei Aufrufe gestartet werden soll (hier: Login)
    ]

    try:
        # Pyinstaller ausführen, falls ein Fehler auftaucht, dann gib eine Warnmeldung
        subprocess.run(command, check=True)
        print(f"Datei: '{output_name}.exe' erfolgreich unter dem Verzeichnis: {dist_path} erstellt.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pyinstaller_module.py <script_path> [output_name]")
        sys.exit(1)

    script_path = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "output"

    create_executable(script_path, output_name)
