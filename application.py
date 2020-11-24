import os
from cs50 import SQL
from flask import Flask, redirect, jsonify, render_template, request, session
from flask_session import Session




app = Flask(__name__)


db = SQL("sqlite:///register.db")
app.config["SESSION_PARMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# login box start here
@app.route("/")
def index():#changed login
    if not session.get("name"):
       return redirect("/login")
    return render_template("index.html")#changed login

@app.route("/search")
def search():
    products = db.execute("SELECT * FROM products WHERE products LIKE ?", "%" + request.args.get("q") + "%s")
    return jsonify(products)


#changed
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #remember that user logid in
        session["name"] = request.form.get("name")
        #redirect user to /
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

######needs some verification of("creating a new database")
#index was here
#######################################
# login box ends here.
#form product


#This is the start of database /email input.
@app.route("/register")
def register():
    rows = db.execute("SELECT * FROM register")
    return render_template("register.html", rows=rows)

@app.route("/registration", methods=["GET","POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide an email address.")
        db.execute("INSERT INTO register (name, email) VALUES (:name, :email)", name=name, email=email)
        return redirect("/register")

#This is the end of email input.




#This is the start of the todo list task
@app.route("/tasks")
def task():
    if "todos" not in session:
        session["todos"] = []
    return render_template("task.html", todos=session["todos"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("tasks")
        session["todos"].append(todo)
        return redirect("/tasks")
#this is the end of the todo list task.




#This is the end of email input.

@app.route("/work", methods=["GET", "POST"])
def work():
    return render_template("work.html")

@app.route("/boot")
def boot():
    return render_template("boot.html")

@app.route("/haa")
def haa():
    return render_template("haa.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")
#the end

# search content
@app.route("/product")
def product():
    return render_template("product.html")

##phonenumber
@app.route("/contact")
def contact():
    rows = db.execute("SELECT * FROM contact")
    return render_template("contact.html", rows=rows)

@app.route("/contacts", methods=["GET","POST"])
def contacts():
    if request.method == "GET":
        return render_template("contacts.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide an email address.")
        phone = request.form.get("phone")
        if not phone:
            return render_template("apology.html", message="You must provide an phone number.")
        db.execute("INSERT INTO contact (name, email, phone) VALUES (:name, :email, :phone)", name=name, email=email, phone=phone)
        return redirect("/contact")

