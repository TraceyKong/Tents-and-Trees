from flask import Flask, render_template, request, redirect, jsonify
from game.PuzzleGenerator import PuzzleGenerator
from game.GameManager import GameManager

app = Flask(__name__)


gameManager = GameManager(None, 5)

@app.route('/', methods=['GET'])
def home():
    grid = gameManager.puzzle
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
    gameManager.play(pos)
    grid = gameManager.puzzle  
    return jsonify(content=grid.getCellValue(pos),status=gameManager.solved)
