from convertJP2ToTiff import convertJP2ToTif
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def call_main():
   convertJP2ToTif(request.args.get('source').split(","))
   return "OK"
