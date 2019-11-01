from flask import Flask
from flask import render_template, url_for, request, redirect, flash


app = Flask("Hello World")


#Beispiel Augabe
@app.route('/hello_simple')
def hello_world_simple():
	return 'Hello, you r the best!'

#Ausgabe/Verlinkung zu html-template
@app.route('/index')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True, port=5000)
	