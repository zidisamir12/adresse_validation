from flask import  Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
	return render_template('index.html')