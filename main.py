from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html', content=[])


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/new.html', methods=['GET', 'POST'])
def new():
    return render_template('new.html')

@app.route('/about.html', methods=['GET'])
def homepage():
    rows = dbHandler.list_moodboards()
    print("Rows:", rows)
    for r in rows:
        print("Row length:", len(r), "Row:", r)

    moodboards_dicts = [
    {
        "moodboard_name": m[0],
        "favourite": (str(m[1]).upper() == "TRUE"),
        "recent": (str(m[2]).upper() == "TRUE"),
        "moodboard_picture": m[3]
    }
    for m in rows
]
    
    recently_opened = [m for m in moodboards_dicts if m["recent"]]
    favourites = [m for m in moodboards_dicts if m["favourite"]]
    others = [m for m in moodboards_dicts if not m["favourite"] and not m["recent"]]
    
    print("Recently opened:", recently_opened)
    print("Favourites:", favourites)
    print("Others:", others)

    return render_template(
        'about.html',
        recently_opened=recently_opened,
        favourites=favourites,
        moodboards=others
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)