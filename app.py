from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

# playlists = [
#     {'title': 'Cat Videos', 'description': 'Cats acting weird'},
#     {'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
#     {'title': "Freddie Mercury's Outfits", 'description': 'Look at that hairy chest!'}
# ]


def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

    def index():
        """Return homepage."""
        return render_template('home.html', msg='Flask is Cool!!')


if __name__ == '__main__':
    app.run(debug=True)