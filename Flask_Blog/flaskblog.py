from flask import Flask , render_template
app = Flask(__name__)

posts = [

	{
		'author':'Joshua Chihozhwa',
		'title':'Married to Medicine',
		'content':'A book about a relationship with a doctor girlfriend',
		'date_posted':'June 1 ,2018'
	},
	{
		'author':'Tsitsi Abokoe Muchokwani',
		'title':'A Lotus Heart',
		'content':'A book about self motivation and self worth',
		'date_posted':'Dec 2 ,2018'
	}
]
@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html',posts =posts)

@app.route("/about")
def about():
	return render_template('about.html',posts =posts)

if __name__ == '__main__':
	app.run(debug=True)