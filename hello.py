from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


# hello world in 127.0.0.1:5000
@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome dear %s' % name


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
