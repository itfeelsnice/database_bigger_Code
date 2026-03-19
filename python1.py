
import sqlite3
from flask import Flask, session, render_template, redirect, request


start1 = Flask(__name__)
start1.secret_key = "123abc456def.,"

# create_db = sqlite3.connect("database1.db")
# execute1 = create_db.cursor()

# execute1.execute("""CREATE TABLE IF NOT EXISTS values1
#                     (collumns INTEGER PRIMARY KEY,
#                     username TEXT)""")

@start1.route("/", methods = ["POST", "GET"])

def def1():
    if request.method == "POST":
        value2 = request.form["inputvalue"]
        if "value1" in session and value2 == session["value1"]:

            create_db = sqlite3.connect("database1.db")
            execute1 = create_db.cursor()

            execute1.execute("""CREATE TABLE IF NOT EXISTS values1(
                                collumns TEXT PRIMARY KEY,
                                username TEXT)""")

            execute1.execute("INSERT INTO values1 (username) VALUES (?)", (value2,))

            create_db.commit()
            create_db.close()

            return redirect("/hello")
        else: 
            return render_template("html1.html", wrong1 = "this value have never seen my session")
    return render_template("html1.html")


@start1.route("/sing up", methods = ["POST", "GET"])
def def2():
    if request.method == "POST":
        value1 = request.form["inputvalue2"]
        if len(value1.strip()) > 0:
            session["value1"] = value1
            return redirect("/")
    return render_template("html2.html")


@start1.route("/hello")
def def3():
    return render_template("html3.html")

start1.run(debug=True)














