from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)

player_oncourt = Blueprint("player_oncourt", __name__, static_folder="static", template_folder="templates")

def playerload():
    variable = True
    if(variable == True):
        print("Hi")