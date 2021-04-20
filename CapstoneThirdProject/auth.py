from flask import Blueprint, render_template
import sqlite3

auth = Blueprint('auth', __name__)

headings = ("Country", "State/Province", "County", "University", "Program", "Requirements")

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT * FROM Uni_Programs_Requ")
data = c.fetchall()


@auth.route('/home')
def home():
    return render_template("home.html", headings=headings, data=data)

@auth.route('/manual')
def manual():
    return render_template("manual.html")

@auth.route('/search')
def search():
    return render_template("search.html")

@auth.route('/details')
def details():
    return render_template("details.html")
    
    