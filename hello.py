from flask import Flask


app = Flask(__name__)


# hello world in 127.0.0.1:5000
@app.route('/')
def index():
    return '<h1>Hello world</h1>'

# starts app
if __name__ == '__main__':
    app.run(debug=True)
