from flask import Flask, render_template

app_folio =  Flask(__name__)

@app_folio.route("/")
def index():
    return render_template("index.html")