from flask import Flask, render_template, request, redirect, jsonify, current_app, url_for
from game.PuzzleGenerator import PuzzleGenerator
from game.GameManager import GameManager
from game.hai import HAI
from game.BasicAI import ComputerAI as BasicAI
from game.RandomAI import RandomAI
from game.ComputerAI import ComputerAI as MRV
import os
from copy import deepcopy
from time import process_time

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
    status = game.checkSolved()

    return jsonify(content=grid.getCellValue(pos), status=status)

############################# Random AI Page ###############################
@app.route('/random-home', methods=['GET','POST'])
def random_home():
    if request.method == 'POST':
        level = request.form['random-level']
        app.config['RANDOM_LEVEL'] = level
        return redirect(url_for('random'))
    else:
        return render_template('random-home.html')

@app.route('/random')
def random():
    app.config['RANDOM-AI'] = RandomAI()
    app.config['GAME'] = GameManager(current_app.config['RANDOM-AI'], int(current_app.config['RANDOM_LEVEL']))

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

    return render_template('random.html', colValues=colValues, content=content, size=size)

@app.route('/solve_random')
def solve_random():
    t0 = process_time()
    app.config['GAME'].start()
    t0 = process_time() - t0

    tents = app.config['GAME'].solution.getTents()

    return jsonify(solved_content=tents, time=t0)

############################# Backtracking AI Page ###############################
@app.route('/backtracking-home', methods=['GET','POST'])
def backtracking_home():
    if request.method == 'POST':
        level = request.form['bt-level']
        app.config['BT_LEVEL'] = level
        return redirect(url_for('backtracking'))
    else:
        return render_template('backtracking-home.html')

@app.route('/backtracking')
def backtracking():
    app.config['BT-AI'] = BasicAI()
    app.config['GAME'] = GameManager(current_app.config['BT-AI'], int(current_app.config['BT_LEVEL']))

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

    return render_template('backtracking.html', colValues=colValues, content=content, size=size)

@app.route('/solve_backtracking')
def solve_backtracking():
    t0 = process_time()
    app.config['GAME'].start()
    t0 = process_time() - t0

    tents = [tent[1] for tent in current_app.config['BT-AI'].solvedTents]

    return jsonify(solved_content=tents, time=t0)

############################# Heuristic Backtracking AI Page ###############################
@app.route('/heuristic-ai-home', methods=['GET','POST'])
def heuristic_ai_home():
    if request.method == 'POST':
        level = request.form['hai-level']
        app.config['HAI_LEVEL'] = level
        return redirect(url_for('heuristic_ai'))
    else:
        return render_template('heuristic-ai-home.html')

@app.route('/heuristic-ai')
def heuristic_ai():
    app.config['GAME'] = GameManager(None, int(current_app.config['HAI_LEVEL']))

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

    return render_template('heuristic-ai.html', colValues=colValues, content=content, size=size)

@app.route('/solve_heuristic_ai')
def solve_heuristic_ai():
    game = deepcopy(current_app.config['GAME'].puzzle)
    hai = HAI(game)
    t0 = process_time()
    app.config['HAI'] = hai.solve()
    t0 = process_time() - t0

    solved_grid = current_app.config['HAI']

    tents = solved_grid.getTents()

    return jsonify(solved_content=tents, time=t0)

############################# MRV AI Page ###############################
@app.route('/mrv-ai-home', methods=['GET','POST'])
def mrv_ai_home():
    if request.method == 'POST':
        level = request.form['mrv-level']
        app.config['mrv_LEVEL'] = level
        return redirect(url_for('mrv-ai'))
    else:
        return render_template('backtracking-home.html')

@app.route('/mrv-ai')
def mrv_ai():
    app.config['MRV-AI'] = MRV()
    app.config['GAME'] = GameManager(current_app.config['MRV-AI'], int(current_app.config['MRV_LEVEL']))

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

    return render_template('mrv-ai.html', colValues=colValues, content=content, size=size)

@app.route('/solve_mrv_ai')
def solve_mrv_ai():
    t0 = process_time()
    app.config['GAME'].start()
    t0 = process_time() - t0

    tents = [tent[1] for tent in current_app.config['MRV-AI'].solvedTents]

    return jsonify(solved_content=tents, time=t0)

############################# ALL AI Page ###############################
@app.route('/all-home', methods=['GET','POST'])
def all_home():
    if request.method == 'POST':
        level = request.form['all-level']
        app.config['ALL_LEVEL'] = level
        return redirect(url_for('all_ai'))
    else:
        return render_template('all-home.html')

@app.route('/all-ai')
def all_ai():
    app.config['GAME'] = GameManager(None, int(current_app.config['ALL_LEVEL']))

    grid = current_app.config['GAME'].puzzle

    colValues = grid.colValues
    content = []
    for r in range(grid.size):
        row = [grid.rowValues[r]]
        cells = [[grid.getCellValue((r, c)), (r,c)] for c in range(len(grid.map[r]))]
        row.append(cells)
        content.append(row)

    size = grid.size

    return render_template('all-ai.html', colValues=colValues, bt_content=content, hai_content=content, mrv_content=content, random_content=content, size=size)

@app.route('/solve_all')
def solve_all():
    # Backtracking AI
    app.config['BT-AI'] = BasicAI()
    app.config['GAME'].player = app.config['BT-AI']

    t0 = process_time()
    app.config['GAME'].start()
    t_backtracking = process_time() - t0

    bt_tents = [tent[1] for tent in current_app.config['BT-AI'].solvedTents]

    # Heuristic Backtracking AI
    current_app.config['GAME'].restart()
    hai = HAI(current_app.config['GAME'].puzzle)
    t0 = process_time()
    app.config['HAI'] = hai.solve()
    t_hai = process_time() - t0

    hai_tents = current_app.config['HAI'].getTents()

    # MRV AI
    current_app.config['GAME'].restart()
    app.config['MRV-AI'] = MRV()
    current_app.config['GAME'].player = app.config['MRV-AI']

    t0 = process_time()
    app.config['GAME'].start()
    t_mrv = process_time() - t0

    mrv_tents = [tent[1] for tent in current_app.config['MRV-AI'].solvedTents]
    
    # Random
    # current_app.config['GAME'].restart()
    # app.config['RANDOM-AI'] = RandomAI()
    # current_app.config['GAME'].player = app.config['RANDOM-AI']

    # t0 = process_time()
    # app.config['GAME'].start()
    # t_random = process_time() - t0

    # random_tents = app.config['GAME'].solution.getTents()

    return jsonify(bt_content=bt_tents, hai_content=hai_tents, mrv_content=mrv_tents, 
                    bt_time=t_backtracking, hai_time=t_hai, mrv_time=t_mrv)