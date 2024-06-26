import os
import time
import json 

from typing import Dict
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.types import UserShort
from os import mkdir, path, sep


with open('./data/ignore.json') as f: people = json.load(f) 


class Bot:

    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password
        self.session = Client()
        self.session.request_timeout = .25
        
    def savedetails(self, tolookup, user_id, flwrs, flwng):
        diff = set(flwng)-set(flwrs)
        date = time.strftime('%Y-%m-%d')
        with open(f'./data/{tolookup}-{date}.json', 'w') as f:
            json.dump({
                'username': tolookup,
                'user_id': user_id,
                'followers': flwrs,
                'following': flwng,
                'diff': list(diff),
                'clean-diff': list(diff-set(people)),
            }, f, indent=4)
        print(f'[INFO]: Saved details for {tolookup} for {date}.')

    def printdetails(self, tolookup, user_id, flwrs, flwng):
        diff = set(flwng)-set(flwrs)
        print('------------------------------------')
        print("username: ", tolookup, "user_id: ", user_id)
        print('------------------------------------')
        print("Followers: ", flwrs)
        print('------------------------------------')
        print("Following: ", flwng)
        print('------------------------------------')        
        print("People you follow but they don't follow you back: ", diff)
        print('------------------------------------')
        print("People you follow but they don't follow you back with removals: ", diff-set(people))
    
    def fastestcompare(self, tolookup: str):
        user_id = self.session.user_id_from_username(tolookup)
        following = self.session.user_following_gql(user_id=user_id)
        followers = self.session.user_followers_gql(user_id=user_id)
        flwng = [follow.username for follow in following]
        flwrs = [follower.username for follower in followers]

        self.printdetails(tolookup, user_id, flwrs, flwng)
        self.savedetails(tolookup, user_id, flwrs, flwng)   
        
        return set(flwng)-set(flwrs)

    def fastcompare(self, tolookup: str):
        user_id = self.session.user_id_from_username(tolookup)
        followers = self.session.user_followers_v1(user_id=user_id)
        following = self.session.user_following_v1(user_id=user_id)
        flwrs = [follower.username for follower in followers]
        flwng = [following.username for following in following]
        
        self.printdetails(tolookup, user_id, flwrs, flwng)
        self.savedetails(tolookup, user_id, flwrs, flwng)

        return set(flwng)-set(flwrs)

    def compare(self, tolookup: str):
        user_id = self.session.user_id_from_username(tolookup)
        followers: Dict[str, UserShort] = self.session.user_followers(user_id=user_id)
        following = self.session.user_following(user_id=user_id)
        flwrs = [ follower.username for follower in followers.values() ]
        flwng = [ following.username for following in following.values() ]
        
        self.printdetails(tolookup, user_id, flwrs, flwng)
        self.savedetails(tolookup, user_id, flwrs, flwng)

        return set(flwng)-set(flwrs)

    def login(self):
        if not path.exists(path=path.dirname(__file__) + f'{sep}/files'):
            mkdir(path=path.dirname(__file__) + f'{sep}/files')
            print('[INFO]: Created files directory.')

        if path.exists(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json'):
            print('[INFO]: Found saved session. Loading...')
            self.session.load_settings(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json') # type: ignore
            logged_in = self.session.login(username=self.username, password=self.password, relogin=True)
        else:
            print('[INFO]: No saved session found. Logging in...')
            logged_in = self.session.login(username=self.username, password=self.password, relogin=True)
            self.session.dump_settings(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json') # type: ignore

        print(f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else '[ERROR]: Failed to log in.')

    def currentworkingdirectory(self):
        print(path.dirname(__file__))
        return path.dirname(__file__)

    def check(self):
        return (self.session.account_info())

if __name__ == '__main__':
    load_dotenv()
    bot = Bot(username=os.getenv('account_name'), password=os.getenv('account_pass'))
    bot.currentworkingdirectory()
    try:
        bot.login()
        bot.compare(tolookup=os.getenv('lookup'))
    except Exception as e:
        print(e)
