import json
import requests
import uuid
import os
from dotenv import load_dotenv
from flask import Flask

from server.bot import Bot

load_dotenv()
app = Flask(__name__)
bot = Bot(username=os.getenv('account_name'), password=os.getenv('account_pass'))

@app.route("/")
def slash():
    return "<p>/</p>"

@app.route("/compare/<username>")
def compare(username):
    bot = Bot(username='scopevariable', password='localvariable')
    bot.currentworkingdirectory()
    bot.login()
    bot.compare(tolookup=username)
    return f"<p>Compare {username}</p>"

if __name__ == '__main__':
    app.run(port=5001, debug=True)
    print('online')
    bot.currentworkingdirectory()