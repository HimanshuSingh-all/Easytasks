from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask( __name__ ) #specify the name of the application and create an instance

#add database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falsess

#Initialise a database
db = SQLAlchemy(app)

# create a model:table
class Todo(db.Model):
	#userid = db.Column(db.Integer,default=1)
	noteid = db.Column(db.Integer,primary_key=True)
	task = db.Column(db.String(200),nullable=False)
	iscomplete= db.Column(db.Boolean,default=False)
	date_added = db.Column(db.DateTime,default=datetime.utcnow)
	
	def __repr__(self):
		return '<Name %r>' %self.task


										# this is basically a get requst below
@app.route('/',methods=['GET','POST']) #this will return the following function's return val to the root to the browser
def welcome():
	return render_template("index.html")



@app.route('/noteadd',methods=['GET','POST'])
def addnote():
	if request.method == 'POST' and 'task' in request.form:
		task=request.form.get('task')
		print(task)
		newtitle=Todo(task=task,iscomplete=False)
		db.session.add(newtitle)
		db.session.commit()

	return render_template('show.html')


@app.route('/tasks',methods=['GET','POST'])
def tasks():
	todo_list=Todo.query.all()
	print(todo_list)
	return render_template('tasks.html',todo_list=todo_list)


@app.route('/delete/<int:noteid>')
def rmtask(noteid):
	print(noteid)
	title=Todo.query.filter_by(noteid=noteid).first()
	db.session.delete(title)
	db.session.commit()

	return redirect( url_for( 'tasks' ) )









if __name__=="__main__":
	with app.app_context():
		db.init_app(app)
		db.create_all()	
		
	app.run(debug=True)


