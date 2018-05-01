from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)
# POSTGRES = {
#     'user': 'flask_user',
#     'pw': 'asad.1234',
#     'db': 'learnflask',
#     'host': 'localhost',
#     'port': '5432',
# }

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_user:asad.1234@localhost:5432/learnflask'

db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("signup.html", form=form)
		else:
			newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()
			return "Success!"
	elif request.method == "GET":
		return render_template("signup.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)