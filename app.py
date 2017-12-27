from flask import Flask, render_template, request, redirect, url_for
from data import Categories, Options
import csv
import datetime

app = Flask(__name__)

Categories = Categories()
Options = Options()

@app.route('/')
def index():
    return render_template('home.html', options=Options)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/categories')
def categories():
    return render_template('categories.html', categories = Categories)

@app.route('/category/<string:id>/')
def category(id):
    return render_template('category.html', id=id)

@app.route('/input', methods = ["POST", "GET"])
def input():
    if request.method == "POST":
        lst_cat = ['food', 'clothes', 'fun']
        with open('text.csv', 'a', newline='') as csvfile:
            swriter = csv.writer(csvfile, delimiter=',')
            for i in lst_cat:
                x = [int(e) for e in request.form[i].split()]
                swriter.writerow([i, sum(x), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")])
        return render_template('category.html')
    else:
        return render_template('input.html')

@app.route('/view')
def view():
    return render_template('view.html', id=id)

if __name__ == "__main__":
    app.run(debug = True)
