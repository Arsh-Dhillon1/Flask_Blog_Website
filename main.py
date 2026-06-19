from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/sleepybloggy"
db = SQLAlchemy(app)
# sno, name, email, phone_number, message, date
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)
    date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        message = request.form.get('message')

        entry = Contacts(name=name, email = email, phone_number=phone_number, message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

app.run()