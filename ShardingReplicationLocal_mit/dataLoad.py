####################################################################################################
# Importieren der Module für DB-Anbindung
####################################################################################################

import sys
import time
import pymongo


####################################################################################################
# Verbindung zu Datenbank-Server oeffnen, wenn nicht verfügbar -> Programmabbruch
####################################################################################################

try:
    dbVerbindung = pymongo.MongoClient("mongodb://mongoAdmin:pkmlp@localhost:30000")
    print("\nVerbindung zu MongoDB erstellt\n")
except pymongo.errors.ConnectionFailure as VerbindungsFehler:
    print("\nKeine Verbindung zu MongoDB: ", VerbindungsFehler, " - Programmabbruch\n")
    sys.exit(1)


####################################################################################################
# Erstellen einer Collection in der Datenbank
####################################################################################################

db = dbVerbindung["myDatabase"]
sammlung = db["myCollection"]


####################################################################################################
# Erstellen von Dokumenten in der Collection in der Datenbank
####################################################################################################

print("Starten des Datenladens ...")

for anzDokumente in range(1,51):
    document = {"AnzDok":"", "Timestamp":"", "Remark":"auto generated test data"}    
    document['AnzDok'] = anzDokumente
    document["Timestamp"] = time.ctime(time.time())
    key = sammlung.insert_one(document)

print("Total:", anzDokumente, "Dokumente wurden geladen")


####################################################################################################
# Schliessen der Datenbank Verbindung
####################################################################################################

print("\nDatenbank Verbindung wird geschlossen\n")
dbVerbindung.close() 
 
 
 