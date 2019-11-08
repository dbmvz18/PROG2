from flask import Flask
from flask import render_template, url_for, request, redirect, flash


app = Flask("Hello World")


#Beispiel Augabe
@app.route('/hello_simple')
def hello_world_simple():
	return 'Hello, you r the best!'

#Ausgabe/Verlinkung zu html-template "index"
@app.route('/index')
def landingpage():
    return render_template('index.html')

#Ausgabe/Verlinkung zu html-template "Übersicht"
@app.route('/uebersicht')
def subpage1():
    return render_template('uebersicht.html')

 #Ausgabe/Verlinkung zu html-template "Subpage2"
@app.route('/apfel')
def subpage2():
    return render_template('#')

 #Ausgabe/Verlinkung zu html-template "Subpage3"
@app.route('/banane')
def subpage3():
    return render_template('#')



if __name__ == "__main__":
	app.run(debug=True, port=5000)
	