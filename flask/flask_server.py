from flask import Flask, request
from subprocess import call

app = Flask(__name__)

@app.route('/')
def call_main():
   args = request.args.get('source').split(",")
   call(["spark-submit","main.py"] + args)
   return "OK"
