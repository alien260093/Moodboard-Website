import random
import database_manager as dbHandler
from flask import Flask, render_template, request, redirect, url_for

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
    if request.method == "POST":
        name = request.form["mname"]

        # Checkbox: present in form only if checked
        favourite = request.form.get("favorite") is not None

        recently_opened = True  # default
        random_image = f"img_{random.randint(1,1000)}.png"

        dbHandler.add_moodboard(name, favourite, recently_opened, random_image)

        return redirect("/about.html")  # or return homepage()

    return render_template('new.html')


@app.route('/about.html', methods=['GET'])
def homepage():
    rows = dbHandler.list_moodboards()

    moodboards_dicts = [
    {
        "moodboard_name": m[0],
        "favourite": str(m[1]).lower() in ("1", "true"),
        "recent": str(m[2]).lower() in ("1", "true"),
        "moodboard_picture": m[3]
    }
    for m in rows
]



    recently_opened = [m for m in moodboards_dicts if m["recent"]]
    favourites = [m for m in moodboards_dicts if m["favourite"]]
    others = [m for m in moodboards_dicts if not m["favourite"] and not m["recent"]]

    return render_template(
        'about.html',
        recently_opened=recently_opened,
        favourites=favourites,
        moodboards=others
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)