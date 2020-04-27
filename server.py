from flask import Flask, request, jsonify
import json
from GameManager import GameManager

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def landing():
    return """<h1>The Landing use this as a test.</h1>"""


@app.route('/start', methods=['POST'])
def start():
    """Creates and solves a puzzle returns solution as a text string"""
    try:
        input = request.get_json()
        player = input['player']
        puzzle_size = input['size']
        puzzle = GameManager(player, size=puzzle_size)
        puzzle.start()
        return puzzle.solution.displayGrid()
    except Exception as e:
        return str(e)

'''
@app.route('/getboard', methods=['GET'])
def getboard():
    try:
        pass
    except Exception as e:
        return str(e)
'''

if __name__ == '__main__':
    # run!
    app.run()