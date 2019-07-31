from app import app
from flask import render_template, request
from app.models import model, formopener
@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")
@app.route('/funny')
def funny():
  return render_template("funny.html")
@app.route('/gifs')
def gifs():
  return render_template("gifs.html")
@app.route('/random')
def random():
  return render_template("random.html")
@app.route('/meme_generator')
def meme_generator():
  return render_template("meme_generator.html")
@app.route('/need_help')
def need_help():
    return render_template("need_help.html")
@app.route('/birthday_month', methods=['GET', 'POST'])
def birthday_month():
   if request.method == 'GET':
       return render_template("birthday_month.html")
   else:
       month = request.form['month']
       if month == "January":
           return "<img src='static/images/January.png' />"
       if month == "February":
           return"<img src='static/images/February.png' />"
       if month == "March":
           return "<img src='static/images/March.jpg' />"
       if month == "April":
           return"<img src='static/images/April.jpg' />"
       if month == "May":
           return "<img src='static/images/May.jpg' />"
       if month == "June":
           return"<img src='static/images/June.jpg' />"
       if month == "July":
           return "<img src='static/images/July.png' />"
       if month == "August":
           return"<img src='static/images/August.jpeg' />"
       if month == "September":
           return "<img src='static/images/September.jpeg' />"
       if month == "October":
           return"<img src='static/images/October.jpg' />"
       if month == "November":
           return "<img src='static/images/November.jpg' />"
       if month == "December":
           return"<img src='static/images/December.jpg' />"