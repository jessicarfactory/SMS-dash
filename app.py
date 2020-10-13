from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from utils import fetch_sms
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, send

load_dotenv()
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!' // Not required when running locally 
Bootstrap(app)
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(fetch_sms):
    sms = fetch_sms()
    return render_template("index.html", sms=sms)


if __name__ == '__main__':
    socketio.run(app)