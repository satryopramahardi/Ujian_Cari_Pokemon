from flask import Flask,jsonify,render_template,request,redirect
import json,requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods= ['POST','GET'])
def find():
    userInput = request.form['userInput']
    if userInput == '':
        return redirect('404.html')
    url = f'https://pokeapi.co/api/v2/pokemon/{userInput}'
    data = requests.get(url)
    if data.status_code == 200:
        dataPokemon = data.json()
        return render_template("pokemon.html",result = dataPokemon)
    else:
        return redirect('404.html')

@app.errorhandler(404)
def notFound(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)
