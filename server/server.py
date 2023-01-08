import json
import requests
import uuid
import os
from dotenv import load_dotenv
from flask import Flask

from bot import Bot
from db import BotBase

app = Flask(__name__)

active_bots = BotBase()


current_bot = active_bots.getfirstbot().data[0]
print(current_bot)

#bot = Bot(username=os.getenv('account_name'), password=os.getenv('account_pass'))
bot = Bot(username=current_bot['username'], password=current_bot['password'])
bot.currentworkingdirectory()
bot.login()

@app.route("/")
def slash():
    return "<p>/</p>"

@app.route("/compare/<username>")
def compare(username):
    print(check())
    compared_set = bot.compare(tolookup=username)
    return json.dumps(list(compared_set))

@app.route("/fastcompare/<username>")
def fastcompare(username):
    print(check())
    compared_set = bot.fastcompare(tolookup=username)
    return json.dumps(list(compared_set))

@app.route('/fastestcompare/<username>')
def fastestcompare(username):
    #print(check())
    compared_set = bot.fastestcompare(tolookup=username)
    print(compared_set)
    return json.dumps(list(compared_set))

@app.route("/pwd")
def pwd():
    return bot.currentworkingdirectory()

@app.route("/check")
def check():
    return bot.check()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    print('online')