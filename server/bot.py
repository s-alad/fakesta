from dotenv import load_dotenv
from instagrapi import Client
import os
from os import getcwd, mkdir, path, sep
from random import choice
import time


class Bot:

    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password
        self.session = Client()
        self.session.request_timeout = .25
    
    def fastestcompare(self, tolookup):
        user_id = self.session.user_id_from_username(tolookup)
        following = self.session.user_following_gql(user_id=user_id)
        followers = self.session.user_followers_gql(user_id=user_id)
        flwng = []
        flwrs = []
        for follow in following:
            flwng.append(follow.username)
        for follower in followers:
            flwrs.append(follower.username)
        print(flwng, flwrs)
        return set(flwng)-set(flwrs)

    def fastcompare(self, tolookup):
        user_id = self.session.user_id_from_username(tolookup)
        followers = self.session.user_followers_v1(user_id=user_id)
        following = self.session.user_following_v1(user_id=user_id)
        flwrs = []
        flwng = []
        for follower in followers:
            flwrs.append(follower.username)
        for following in following:
            flwng.append(following.username)
        print('------------------------------------')
        print(flwrs, flwng)
        return set(flwng)-set(flwrs)

    def compare(self, tolookup):
        user_id = self.session.user_id_from_username(tolookup)
        followers = self.session.user_followers(user_id=user_id)
        following = self.session.user_following(user_id=user_id)
        flwrs = []
        flwng = []
        for follower in followers.values():
            flwrs.append(follower.username)
        for following in following.values():
            flwng.append(following.username)
        
        print('------------------------------------')
        print("username: ", tolookup, "user_id: ", user_id)
        print('------------------------------------')
        print("Followers: ", flwrs)
        print('------------------------------------')
        print("Following: ", flwng)
        print('------------------------------------')        
        print("People you follow but they don't follow you back: ", set(flwng)-set(flwrs))

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
        print(bot.fastestcompare('csynikl'))
    except Exception as e:
        print(e)
 