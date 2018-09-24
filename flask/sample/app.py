import numpy
from flask import Flask,render_template,request,redirect,url_for,abort

import logging
import logging.handlers

from model.user import User
from database import init_db,db_session

app = Flask(__name__)

#log will be output to log folder
handler = logging.handlers.RotatingFileHandler("log/test.log","a+",maxBytes=3000, backupCount = 5)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(handler)

def pick_up():
 messages = [ "hello!",
 "Good Moreing",
 "Good Night!"
 ]
 return numpy.random.choice(messages)

@app.route("/")
def index():
    app.logger.info("here is index")
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

#sqlalchemy : select all
@app.route("/users",methods = ['GET'])
def all_users():
    users = User.query.all()
    return render_template("users.html",users=users)

#sqlalchemy : filter
@app.route("/user/<name>",methods = ['GET'])
def show_user(name):
    user = User.query.filter_by(name = name).first()
    if user is None:
        abort(404)
    return render_template("user.html",user=user)

#Keep in mind that teardown callbacks are always executed
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/user",methods =["POST"])
def post_content():
    name = request.form["name"]
    fullname = request.form["fullname"]
    password = request.form["password"]

    user = User.query.filter_by(name=name).first()
    if user is None:
        user = User(name,fullname,password)
    else:
        user.name = name
        user.fullname = fullname
        user.password = password
    
    db_session.add(user)
    db_session.commit()
    return redirect(url_for('all_users'))

# 
init_db()
if __name__ == "__main__":
    #init_db() #=>in here can't create tables!!
    app.debug = True
    app.run(host = '0.0.0.0') # can access from anywhere