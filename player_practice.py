from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)

player_practice = Blueprint("player_practice", __name__, static_folder="static", template_folder="templates")

def playerload():
    variable = True
    if(variable == True):
        print("Hi")