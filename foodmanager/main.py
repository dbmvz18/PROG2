from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import data_foodmanager

app = Flask("foodmanager")



#Ausgabe/Verlinkung zu html-template "Startseite
@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')



#Ausgabe/Verlinkung zu html-template "Übersicht": hier werden sämtliche erfasste Daten, Nahrungsmittel (NM) und Ablaufdatum (AD), ausgegeben
@app.route('/uebersicht')
def uebersicht():
    return render_template('uebersicht.html')



 #Ausgabe/Verlinkung zu html-template "Verwaltung": hier werden die Daten (NM und AD) erfasst und in Dictionary gespeichert
@app.route('/hinzufuegen', methods=['GET', 'POST'])
def hinzufuegen():
    if (request.method == 'POST'):
        data_foodmanager.eintrag_speichern_von_formular(request.form)
        return redirect("/")
    return render_template('hinzufuegen.html')



#Ausgabe/Verlinkung zu html-template "Suchen"
@app.route("/suchen/<name>")
@app.route("/suchen", methods=['GET', 'POST'])
def suchen(name=None):
    if (request.method == 'POST'):
        nahrungsmittel = data_foodmanager.nahrungsmittel_suchen(request.form)
        print(nahrungsmittel)
        return render_template("uebersicht.html", dictfoodmanager=nahrungsmittel)

    return render_template("suchen.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)
    