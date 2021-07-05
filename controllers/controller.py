from flask import render_template
from app import app
from models.game import *
from models.player import *


@app.route("/")
def index():
    return render_template("index.html", title = "Rock-Paper-Scissors", players=players)

@app.route("/winner")
def winner():
    return render_template("winner.html", title = "the winner")