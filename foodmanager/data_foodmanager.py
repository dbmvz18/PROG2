import json
import datetime
import main


filename = "data_foodmanager_db.txt"
#Funktion, um Einträge des Benutzers auf "Übersicht" zu lesen ("r) und auszugeben
def data_foodmanager_lesen():
    data = {}
    try:
        with open(filename, "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data



#Funktion, um Einträge des Benutzers auf "Verwalten" zu schreiben ("w")
def data_foodmanager_schreiben(daten):
    with open(filename, "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)




#Funktion, um Einträge des Benutzers in der Datei "data_foodmanager.txt" zu speichern (Dictionary: Key=Nahrungsmittel, Value=Ablaufdatum)
def eintrag_speichern(nahrungsmittel, ablaufdatum):
    data_foodmanager = data_foodmanager_lesen()
    data_foodmanager[nahrungsmittel] = {"nahrungsmittel": nahrungsmittel, "ablaufdatum": ablaufdatum, "benachrichtigung": False}
    print(data_foodmanager)
    data_foodmanager_schreiben(data_foodmanager)
#Variabeln frei wählbar




#Funktion, um "neue" Einträge des Benutzers über das Formular entgegenzunehmen und an Funktion "eintrag_speichern" zur definitiven Speicherung weiterzugeben
def eintrag_speichern_von_formular(form_request):
    print(form_request)
    nahrungsmittel = form_request.get('nahrungsmittel')
    ablaufdatum = form_request.get('ablaufdatum')
    eintrag_speichern(nahrungsmittel, ablaufdatum)




#Funktion, um Einträge des Benutzers zu löschen
def eintrag_entfernen(id):
    data_foodmanager = data_foodmanager_lesen()
    data_foodmanager.pop(id)
    data_foodmanager_schreiben(data_foodmanager)




#Funktion, um Einträge des Benutzers zu suchen und anschliessend auszugeben
def nahrungsmittel_suchen(form_request):
    data_foodmanager = data_foodmanager_lesen()
    nahrungsmittel = form_request.get('nahrungsmittel')

    if nahrungsmittel in data_foodmanager:
        return {nahrungsmittel: data_foodmanager[nahrungsmittel]}
#Variabeln frei wählbar




# Funktion, um Fälligkeit (Ablaufdatum = heute) festzustellen, "False" mit "True" (Key: benachrichtigung, value: False) zu ersetzen und anschliessend E-Mail versenden
def avocado():
    data_foodmanager = data_foodmanager_lesen()
    heute = datetime.datetime.today()

    for key, values in data_foodmanager.items():
        datetime_str = values['ablaufdatum']
        datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
        if datetime_obj <= heute:
            if not values['benachrichtigung']:
                notification()

                # False wird durch True ersetzt (damit Nachricht bei nächstem Durchlauf nicht erneut gesendet wird)
                data_foodmanager[key]['benachrichtigung'] = True

    data_foodmanager_schreiben(data_foodmanager)
