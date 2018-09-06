from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World , I am Flask! Test me"

'''
How to run:

$ export FLASK_APP=hello_world.py
$ export FLASK_ENV=development
$ flask.run
'''
