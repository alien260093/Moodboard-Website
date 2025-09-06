from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/test')
def test():
    return "Test route works!"

if __name__ == "__main__":
    app.run(debug=True)
