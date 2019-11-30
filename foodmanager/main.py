from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
import datetime



from libs import data_foodmanager

app = Flask("foodmanager")


# Anzeige in URL, bspw. .http://127.0.0.1:5000/ueber (@app.route: /, /index, /verwalten, /hinzufuegen, /uebersicht, /suchen)
# Kommuniziert mit url-for in Navigation (header.html): def: index():, ueber():, verwalten():, hinzufuegen():, uebersicht():, suchen():


#Ausgabe/Verlinkung zu html-template "Startseite"
@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')


#Ausgabe/Verlinkung zu html-template "Über" (Geschichte des Food-Manager)
@app.route('/ueber')
def ueber():
    return render_template('ueber.html')



#Ausgabe/Verlinkung zu html-template "Verwalten": hier werden sämtliche erfasste Daten, Nahrungsmittel (NM) und Ablaufdatum (AD), ausgegeben. Zugleich können diese hier entfernt werden.
@app.route('/verwalten')
@app.route('/verwalten', methods=['GET', 'POST'])
def verwalten():
    fmdaten = data_foodmanager.data_foodmanager_lesen()
    return render_template('verwalten.html', dictfoodmanager=fmdaten)

    if (request.method == 'POST'):
            data_foodmanager.eintrag_speichern_von_formular(request.form)
            return redirect("/verwalten") #Befehl um nach Drücken des "Hinzufügen"-Buttons zu Übersichtsliste zu gelangen



#Erfassung auf "Verwalten" funktioniert noch nicht




#Ausgabe/Verlinkung zu html-template "hinzufügen": hier werden die Daten (NM und AD) erfasst und in Dictionary gespeichert
@app.route('/hinzufuegen', methods=['GET', 'POST'])
def hinzufuegen():
    if (request.method == 'POST'):
        data_foodmanager.eintrag_speichern_von_formular(request.form)
        return redirect("/verwalten") #Befehl um nach Drücken des "Hinzufügen"-Buttons zu Übersichtsliste zu gelangen
    return render_template('hinzufuegen.html')




# Verlinkung bzw. Funktion, um per "Entfernen"-Button, Einträge aus Dictionary zu löschen
@app.route('/delete/<id>')
def entfernen(id=None):
    if id:
        print(id)
        data_foodmanager.eintrag_entfernen(id)

    return redirect(request.referrer) #Befehl, um auf vorherige Seite zurückzukehren



#Ausgabe/Verlinkung zu html-template "Übersicht" (Grundlage für Benachrichtigung): Erfasste Daten werden strukturiert und sortiert nach Datum ausgegeben
@app.route('/uebersicht')
def uebersicht():
    fmdaten = data_foodmanager.data_foodmanager_lesen()
    return render_template('uebersicht.html', dictfoodmanager=fmdaten)



#Ausgabe/Verlinkung zu html-template "Suchen"
@app.route("/suchen/<name>")
@app.route("/suchen", methods=['GET', 'POST'])
def suchen(name=None):
    if (request.method == 'POST'):
        nahrungsmittel = data_foodmanager.nahrungsmittel_suchen(request.form)
        print(nahrungsmittel)
        return render_template("verwalten.html", dictfoodmanager=nahrungsmittel)

    return render_template("suchen.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)
    