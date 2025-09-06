from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['GET'])
def index():
    data = dbHandler.listExtension()
    return render_template('index.html', content=data)


@app.route('/add.html', methods=['GET', 'POST'])
def login():
    return render_template('add.html')

@app.route('/about.html', methods=['GET', 'POST'])
def homepage():
    all_moodboards = dbHandler.listExtension()  # This returns tuples
    recently_opened = [m for m in all_moodboards if m[5] == 1]
    favourites = [m for m in all_moodboards if m[4] == 1]
    others = [m for m in all_moodboards if m[5] == 0 and m[4] == 0]
    return render_template(
        'about.html',
        recently_opened=recently_opened,
        favourites=favourites,
        moodboards=others
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
  