from flask_script import Manager
from flask import Flask

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def entry():
    return '<h1>I am on another port now</h1>'

if __name__ == '__main__':
    manager.run()