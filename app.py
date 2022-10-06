from flask import Flask, request, render_template


app = Flask( __name__ ) #specify the name of the application and create an instance



				# this is basically a get requst below
@app.route('/') #this will return the following function's return val to the root to the browser
def welcome():
	return render_template("index.html")

@app.route('/noteadd',methods=['GET','POST'])
def addnote():
	return render_template('show.html')



@app.route('/methods', methods=['GET', 'POST'])
def methodcheck():
	
	if request.method=='GET':
		return 'YOu are using a GET method'

	if request.method=='POST':
		return 'YOU are using a POST method'

app.run(debug=True)


