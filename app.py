from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)



@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)


if __name__ == '__main__':
    app.run(debug=True)