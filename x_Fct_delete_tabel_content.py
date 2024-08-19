'''
In diesem Modul können die Werte aus den Tabellen der Datenbank gelöscht werden. Dies hat auch keinen
Zusammenhang mit dem eigentlichen Programm. Es dient lediglich zur Löschung der Daten die beim Testverfahren entstehen.
'''


import sqlite3


def clear_database():
    # Verbindung zur SQLite-Datenbank herstellen
    mydb = sqlite3.connect('Database.db')
    cursor = mydb.cursor()

    # Tabelle Account leeren
    cursor.execute('DELETE FROM Account')

    # Tabelle Prioritäten leeren
    cursor.execute('DELETE FROM Prioliste')

    # Tabelle Personalliste leeren
    cursor.execute('DELETE FROM Personalliste')

    # Tabelle Schichtpläne leeren
    cursor.execute('DELETE FROM Schichtpläne')


    # Änderungen speichern und Verbindung schließen
    mydb.commit()
    mydb.close()

    print("Tabelle geleert.")

# Ausführen (Achtung! Daten werden unwiderruflich gelöscht)
# clear_database()