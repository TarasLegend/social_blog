from flask import Flask


app = Flask(__name__)


# hello world in 127.0.0.1:5000
@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome dear %s' % name


if __name__ == '__main__':
    app.run(debug=True)
