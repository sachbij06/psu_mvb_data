from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)

team_oncourt = Blueprint("team_oncourt", __name__, static_folder="static", template_folder="templates")
