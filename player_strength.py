from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)

player_strength = Blueprint("player_strength", __name__, static_folder="static", template_folder="templates")
