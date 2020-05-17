from flask import Flask, render_template, request, redirect, jsonify, current_app
from game.PuzzleGenerator import PuzzleGenerator
from game.GameManager import GameManager

app = Flask(__name__)
app.config['GAME'] = GameManager(None, 5)

@app.route('/', methods=['GET'])
def home():
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
    return render_template('home.html', colValues=colValues, content=content, size=size)

@app.route('/get_move')
def get_move():
    pos = request.args.get('pos', '')[1:-1]
    pos = pos.split(',')
    pos = (int(pos[0]), int(pos[1]))
    game = current_app.config['GAME']
    game.play(pos)
    grid = current_app.config['GAME'].puzzle  
    return jsonify(content=grid.getCellValue(pos),status=game.solved)
