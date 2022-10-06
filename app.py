from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask( __name__ ) #specify the name of the application and create an instance

#add datdbase
#app.config['SQL_ALCHEMY_URI']='sqlite///users.db'

#app.config['SQL_ALCHEMY_URI']='sqlite///notes.db'

#app.config['SECRET_KEY']='outlook_23@orkut'

#Initialise a database
#db = SQLAlchemy(app)
"""

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default="My Notebook")
    password = db.Column(db.String(100), default=None)
    last_modified = db.Column(db.DateTime, default=datetime.datetime.today())


# create a model:
class notes(db.model):
	userid = db.column()
	noteid = db.column(db.Integer,primary=True)
	title = db.column(db.string(200))
	date_added = db.column()
"""


				# this is basically a get requst below
@app.route('/',methods=['GET','POST']) #this will return the following function's return val to the root to the browser
def welcome():
	return render_template("index.html")

@app.route('/noteadd',methods=['GET','POST'])
def addnote():
	return render_template('show.html')


@app.route('/tasks',methods=['GET','POST'])
def tasks():
	return render_template('tasks.html')


@app.route('/methods', methods=['GET', 'POST'])
def methodcheck():
	
	if request.method=='GET':
		return 'YOu are using a GET method'

	if request.method=='POST':
		return 'YOU are using a POST method'

app.run(debug=True)


