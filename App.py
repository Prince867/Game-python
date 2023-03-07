from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = ''
    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result = "You win!"
    elif player_choice == 'paper' and computer_choice == 'rock':
        result = "You win!"
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result = "You win!"
    else:
        result = "You lose!"
    return render_template('play.html', 
                           player_choice=player_choice, 
                           computer_choice=computer_choice, 
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
