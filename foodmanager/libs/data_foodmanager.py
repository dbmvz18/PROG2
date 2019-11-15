import json

def data_foodmanager_lesen():
    data = {}
    try:
        with open('data_foodmanager.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

#Funktion, um Einträge des Benutzers zu lesen und auszugeben
def eintrag_speichern(nahrungsmittel, ablaufdatum):
    data_foodmanager = data_foodmanager_lesen()
    data_foodmanager[nahrungsmittel] = {"nahrungsmittel": nahrungsmittel, "ablaufdatum": ablaufdatum}
    print(data_foodmanager)
    with open('data_foodmanager.txt', "w", encoding="utf-8") as open_file:
        json.dump(data_foodmanager, open_file)


#Funktion, um Einträge des Benutzers zu speichern und anschliessend zu öffnen
def eintrag_speichern_von_formular(form_request):
    print(form_request)
    nahrungsmittel = form_request.get('nahrungsmittel')
    ablaufdatum = form_request.get('ablaufdatum')
    eintrag_speichern(nahrungsmittel, ablaufdatum)



def nahrungsmittel_suchen(form_request):
    data_foodmanager = data_foodmanager_lesen()
    nahrungsmittel = form_request.get('nahrungsmittel')

    if nahrungsmittel in data_foodmanager:
        return {nahrungsmittel: data_foodmanager[nahrungsmittel]}