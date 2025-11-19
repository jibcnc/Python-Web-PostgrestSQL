from flask import Flask, render_template
from query_db import my_select

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")   

@app.route("/movie")
def movie_list():
    contacts = my_select()                 
    return render_template("movie.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)
