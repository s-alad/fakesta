from instagrapi import Client
from os import getcwd, mkdir, path, sep
from random import choice

class Bot:

    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password
        self.session = Client()

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
        
        print("Followers: ", flwrs)
        print('------------------------------------')
        print("Following: ", flwng)
        print('------------------------------------')        
        print("People you follow but they don't follow you back: ", set(flwng)-set(flwrs))

    def login(self):
        if not path.exists(path=path.dirname(__file__) + f'{sep}/files'):
            mkdir(path=path.dirname(__file__) + f'{sep}/files')
            print('[INFO]: Created files directory.')

        if path.exists(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json'):
            print('[INFO]: Found saved session. Loading...')
            self.session.load_settings(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json') # type: ignore
            logged_in = self.session.login(username=self.username, password=self.password)
        else:
            print('[INFO]: No saved session found. Logging in...')
            logged_in = self.session.login(username=self.username, password=self.password)
            self.session.dump_settings(path=path.dirname(__file__) + sep + 'files' + sep + f'{self.username}.json') # type: ignore

        print(f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else '[ERROR]: Failed to log in.')

    def currentworkingdirectory(self):
        print(path.dirname(__file__))
        return path.dirname(__file__)
