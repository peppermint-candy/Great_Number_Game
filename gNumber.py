from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "Secret"


@app.route('/')
def index():

	if "num" in session:
		pass
	else:
		session['num'] = random.randrange(0,101)
	print session['num']
	return render_template("index.html")


@app.route('/check', methods=['POST'])
def lower():

	session['guess'] = request.form['guess']
	if int(session['guess']) == session['num']:
		session['message'] = session['guess']+" was the number!"
		session['reset'] = True
		session.pop('guess')
		return render_template('index.html')
	elif int(session['guess']) > session['num']:
		session['message'] = "Too high!"
		return render_template('index.html')
	elif int(session['guess']) < session['num']:
		session['message'] = "Too Low!"
		return render_template('index.html')
	else:
		session['message'] = ""


@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)