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
    # Mock data to simulate DB response
    all_moodboards = [
        (1, "Summer Vibes", 1, 0, "Extra data", "/static/images/summer.jpg"),
        (2, "Winter Mood", 0, 1, "Extra data", "/static/images/winter.jpg"),
        (3, "Spring Colors", 0, 0, "Extra data", "/static/images/spring.jpg")
    ]

    # Convert to dictionaries (like before)
    moodboards_dicts = [
        {
            "id": m[0],
            "name": m[1],
            "favourite": m[2],
            "recently_opened": m[3],
            "extra": m[4],
            "image": m[5]
        }
        for m in all_moodboards
    ]

    # Filter into categories
    recently_opened = [m for m in moodboards_dicts if m["recently_opened"] == 1]
    favourites = [m for m in moodboards_dicts if m["favourite"] == 1]
    others = [m for m in moodboards_dicts if not m["favourite"] and not m["recently_opened"]]

    return render_template(
        'about.html',
        recently_opened=recently_opened,
        favourites=favourites,
        moodboards=others
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/test')
def test():
    print("Test route is running!")
    return "Test route works!"