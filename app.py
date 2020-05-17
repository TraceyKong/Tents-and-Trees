from flask import Flask, render_template, request, redirect, jsonify, current_app, url_for
from game.PuzzleGenerator import PuzzleGenerator
from game.GameManager import GameManager
from simpleForm import LevelForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        level = request.form['level']
        app.config['LEVEL'] = level
        return redirect(url_for('game'))
    else:
        return render_template('home.html')

@app.route('/game')
def game():
    app.config['GAME'] = GameManager(None, int(current_app.config['LEVEL']))
    grid = current_app.config['GAME'].puzzle

    grid.displayGrid()

    colValues = grid.colValues
    content = []
    for r in range(grid.size):
        row = [grid.rowValues[r]]
        cells = [[grid.getCellValue((r, c)), (r,c)] for c in range(len(grid.map[r]))]
        row.append(cells)
        content.append(row)
    size = grid.size

    return render_template('game.html', colValues=colValues, content=content, size=size)

@app.route('/get_move')
def get_move():
    pos = request.args.get('pos', '')[1:-1]
    pos = pos.split(',')
    pos = (int(pos[0]), int(pos[1]))

    game = current_app.config['GAME']
    game.play(pos)
    grid = game.puzzle
    status = game.solved

    return jsonify(content=grid.getCellValue(pos), status=status, grid=grid.map)
