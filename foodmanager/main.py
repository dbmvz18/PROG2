from flask import Flask, session
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
import os
import datetime


from libs import data_foodmanager

app = Flask("foodmanager")
#Notwendig um Alerts (flash) zu aktivieren
app.secret_key ="super secret key"


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

#Anzeige eines "Alerts" nach Hinzufügen
        if request.method == 'POST':
            flash("Nahrungsmittel erfolgreich hinzugefügt!", "success")
            return redirect("/verwalten")

        return redirect("/verwalten") #Befehl um nach Drücken des "Hinzufügen"-Buttons zu Übersichtsliste zu gelangen
    return render_template('hinzufuegen.html')




# Verlinkung bzw. Funktion, um per "Entfernen"-Button, Einträge aus Dictionary zu löschen
@app.route('/delete/<id>')
def entfernen(id=None):
    if id:
        print(id)
        data_foodmanager.eintrag_entfernen(id)

#Anzeige eines "Alerts" nach Entfernen
        flash("Nahrungsmittel erfolgreich entfernt!", "success")
        return redirect("/verwalten")

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

#Anzeige eines "Alerts" wenn Benutzereingabe nicht gefunden wird
        if nahrungsmittel:
            flash("Nahrungsmittel gefunden!", "success")
        else:
            flash("Nahrungsmittel nicht gefunden! Überprüfe deine Eingabe!", "danger")

        return render_template("/verwalten.html", dictfoodmanager=nahrungsmittel)

    return render_template("suchen.html")



#Ausgabe/Verlinkung zu html-template "Baustelle" (inaktive interne Seite)
@app.route("/Baustelle")
def baustelle():
    return render_template('baustelle.html')




#Notification per E-Mail über Python ausgeben (gmail-account)
from flask import Flask
from flask_mail import Mail
from flask_mail import Message

#app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'rony.hanselmann@gmail.com'
app.config['MAIL_PASSWORD'] = 'uxhulfusqzatbmno'
app.config['MAIL_DEFAULT_SENDER'] = 'rony.hanselmann@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False


mail = Mail(app)
#mail = Mail()
#mail.init_app(app)


#Benachrichtigung per E-Mail (Flask-Mail)
@app.route("/notification")
def notification():

    msg = Message(
            subject = 'Food-Manager',
            recipients = ['rony.hanselmann@adon.li'],
            body = 'Nahrungsmittel läuft ab!',
            #date = 'date',
            #extra_headers = {'nahrungsmittel': 'ablaufdatum'}
            )

    #msg = Message('Food-Manager', recipients=['rony.hanselmann@adon.li'])
    #msg.body = "Das ist eine Test-Notification von Rony's Web-Applikation. Bitte nicht antworten!"
   
    
    with app.open_resource('static/pics/notification.jpeg') as notification:
        msg.attach('static/pics/notification.jpeg', 'image/jpeg', notification.read())

    #mail.send(msg)

    

    return 'Nachricht gesendet!'
    return render_template('notification.html')


#Umleitung zu Startseite, nach Aufrufen nicht vorhandener URLs
@app.errorhandler(404)
def page_not_found(e):
    return redirect('http://127.0.0.1:5000/')  

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    