# Om Namah Shivaya.

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
