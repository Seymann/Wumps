from flask import Flask
from flask import request
from flask import render_template
from wumpsGame import WumpsGame
from flask import make_response
import json
import datetime

app = Flask(__name__)


@app.route('/game/<game>')
def show_game(game=None, extramessage=None):
    global gameDict
    if game is None and 'game' in request.form:
        game = request.form['game']
    if game in gameDict:
        phase = gameDict[game].phase

        if not gameDict[game].playerList:
            pointedAt = "None"
        else:
            pointedAt = gameDict[game].playerList[gameDict[game].pointer]

        counter = gameDict[game].roundcounter

        playersandscores = []
        for player in gameDict[game].turnDict:
            playersandscores.append( (player, str(gameDict[game].turnDict[player]['fucked'])) )

        timestring = datetime.datetime.now().astimezone().isoformat()

        if extramessage is not None:
            return render_template('game.html', name=game, phase=phase, playerList=playersandscores, pointedAt=pointedAt, counter=counter, extramessage=extramessage, timestring=timestring)
        else:
            return render_template('game.html', name=game, phase=phase, playerList=playersandscores, pointedAt=pointedAt, counter=counter, timestring=timestring)
    else:
        return render_template('no_game.html', name=game)


@app.route('/game', methods = ['GET', 'POST'])
def game():
    if request.method == 'GET':
        game = request.args['game']
        return show_game(game)
    elif 'game' in request.form:
        game = request.form['game']
        return post_game(game, request.form, True)

    return "Please Specify a Game!"


@app.route('/game/<game>', methods=['POST'])
def post_game(game=None, dict=None, inServer=False):
    # possible Actions: add Player, take turn, reset
    global gameDict
    if not inServer:
        dict = request.form

    if game is None and 'game' in dict:
        game = dict['game']
    if game in gameDict:
        if 'type' in dict:
            theType = dict['type']
            if theType == "reset":
                gameDict[game].reset()
                return show_game(game, "Reset the game, u sly fox")

            elif theType == "addName":
                #TODO add chekc if name already given!
                if 'name' in dict:
                    Ourname = dict['name']
                else:
                    Ourname = request.cookies.get('Name')
                gameDict[game].addName(Ourname)
                return show_game(game, "Added a new name: {}.. i would recommend removing him again.".format(Ourname))

            elif theType == "taketurn":
                if 'name' not in dict:
                    name = request.cookies.get('Name')
                else:
                    name = dict['name']
                if 'turn' in dict:

                    gameDict[game].takeTurn(name, dict['turn'])
                    return show_game(game, "Taken the Turn {}. Bad Idea.".format(dict['turn']))
                return "Damn Daniel. Kys"

    return "U Fucked Up"


@app.route('/')
def home():
    name = request.cookies.get('Name')
    if name == None:
        return render_template('home.html')
    else:
        return render_template('home.html', name=name)


@app.route('/setname', methods = ['POST', 'GET'])
def set_name():
    print(request.form)
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('home.html', name=user))
        resp.set_cookie('Name', user)
        return resp

    return render_template('home.html')


@app.route('/getname')
def get_name():
    name = request.cookies.get('Name')
    return 'Welcome {} '.format(name)


@app.route('/', methods=['POST'])
def handle_post():
    global gameDict
    if 'type' in request.form and 'game' in request.form:
        theType = request.form['type']

        if theType == "newgame":
            game = WumpsGame()
            gameDict[request.form['game']] = game
            return show_game(request.form['game'])

        if request.form['game'] in gameDict:
            currGame = gameDict[request.form['game']]
            if theType == "reset":
                currGame.reset()
                return 'SUCC'

            elif theType == "addName":
                #TODO add chekc if name already given!
                if 'name' in request.form:
                    currGame.addName(request.form['name'])
                    return 'SUCC'
                return 'Failed Post!'

            elif theType == "taketurn":
                if 'name' in request.form and 'turn' in request.form:
                    currGame.takeTurn(request.form['name'], request.form['turn'])
                    return 'SUCC'
                return 'Failed Post!'

    return 'Failed Post!'


if __name__ == "__main__":
    gameDict = {}
    app.run(port=5000)