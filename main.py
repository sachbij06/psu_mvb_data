from flask import Flask, render_template
from player_oncourt import player_oncourt
from player_strength import player_strength
from team_oncourt import team_oncourt
from team_strength import team_strength
import webbrowser


app = Flask(__name__)
app.register_blueprint(player_oncourt, url_prefix="")
app.register_blueprint(player_strength, url_prefix="")
app.register_blueprint(team_oncourt, url_prefix="")
app.register_blueprint(team_strength, url_prefix="")

@app.route('/home')
def dashboard():
    return render_template('index.html')

@app.route('/player_oncourt')
def playerpractice():
    return render_template('player_oncourt.html')

@app.route('/player_strength')
def playerstrength():
    return render_template('player_strength.html')
                           
@app.route('/team_oncourt')
def teampractice():
    return render_template('team_oncourt.html')

@app.route('/team_strength')
def teamstrength():
    return render_template('team_strength.html')
                           

if __name__ == '__main__':
    app.run('127.0.0.1', 4000, debug=True)
    webbrowser.open("http://127.0.0.1:4000/home")
