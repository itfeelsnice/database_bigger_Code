
import sqlite3
from flask import Flask, session, render_template, redirect, request


start1 = Flask(__name__)
start1.secret_key = "123abc456def.,"

@start1.route("/", methods = ["POST", "GET"])
def.def1():
    if request.method == "POST":

























