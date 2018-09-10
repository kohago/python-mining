import numpy
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

def pick_up():
 messages = [ "hello!",
 "Good Moreing",
 "Good Night!"
 ]
 return numpy.random.choice(messages)

@app.route("/")
def index():
    title = "this is test title!"
    messages = pick_up()
    return render_template('index.html',messages=messages, title=title)


@app.route("/post",methods = ['GET' , 'POST'])
def post():
    title = "there is a post"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',name=name, title=title)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0') # can access from anywhere
