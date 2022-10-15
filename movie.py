import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/list', methods=['GET'])
def list():
    movie = request.args.get('name')
    response = requests.get(f'https://www.omdbapi.com/?s={movie}&apikey=1ed30124')
    r = response.json()
    if r["Response"] == "False":
        error = r['Error']
        return render_template('error.html', error=error)
    else:
        search = r['Search']
        return render_template('list.html',search=search)

@app.route('/movie', methods=['GET']) 
def search():
    movie = request.args.get('name')
    response = requests.get(f'https://www.omdbapi.com/?t={movie}&apikey=1ed30124')
    r = response.json()
    title = r['Title']
    released = r['Released']
    poster = r['Poster']
    imdb = r['imdbRating']
    runtime = r['Runtime']
    genre = r['Genre']
    overview = r['Plot']
    imdb_id = r['imdbID']
    ratings = r['Ratings']
    return render_template('movie.html', ratings=ratings, imdb_id=imdb_id, overview=overview, title=title, poster=poster, released=released, imdb=imdb, runtime=runtime, genre=genre)

app.run(debug=True)
