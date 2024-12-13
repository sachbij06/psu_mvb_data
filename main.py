from flask import Flask, render_template
from player_practice import player_practice
from player_strength import player_strength
from team_practice import team_practice
from team_strength import team_strength


app = Flask(__name__)
app.register_blueprint(player_practice, url_prefix="")
app.register_blueprint(player_strength, url_prefix="")
app.register_blueprint(team_practice, url_prefix="")
app.register_blueprint(team_strength, url_prefix="")

@app.route('/home')
def dashboard():
    return render_template('index.html')

@app.route('/player_practice')
def playerpractice():
    return render_template('player_practice.html')

@app.route('/player_strength')
def playerstrength():
    return render_template('player_strength.html')
                           
@app.route('/team_practice')
def teampractice():
    return render_template('team_practice.html')

@app.route('/team_strength')
def teamstrength():
    return render_template('team_strength.html')
                           

if __name__ == '__main__':
    app.run('127.0.0.1', 4000, debug=True)
