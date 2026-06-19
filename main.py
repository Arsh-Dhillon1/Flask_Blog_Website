from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/sleepybloggy"
db = SQLAlchemy(app)

class Contacts(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

app.run()