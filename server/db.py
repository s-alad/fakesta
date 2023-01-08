from dotenv import load_dotenv
import os
from supabase import create_client, Client
from bot import Bot

load_dotenv()

class BotBase:
    def __init__(self):
        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_KEY')
        self.table = os.getenv('SUPABASE_TABLE')
        self.supabase: Client = create_client(self.url, self.key)

    def find(self) -> dict:
        data = self.supabase.table(self.table).select("*").execute()
        if data != 0: return data
        else: return None
    
    def getbot(self, id) -> dict:
        data = self.supabase.table(self.table).select("*").eq('id', id).execute()

    def getfirstbot(self) -> dict:
        data = self.supabase.table(self.table).select("*").limit(1).execute()
        if data != 0: return data
        else: return None

    def getlastbot(self) -> dict:
        data = self.supabase.table(self.table).select("*").order(column='id', desc=True).limit(1).execute()
        if data != 0: return data
        else: return None

    def insertbot(self, username: str, password: str):
        print('INSERTING...')
        return self.supabase.table(self.table).insert({"username": username, "password": password}).execute()

    def deletebot(self, id):
        print('DELETING...')
        return self.supabase.table(self.table).delete().eq('id', id).execute()

    def deletefirstbot(self):
        print('DELETING FIRST...')
        return self.supabase.table(self.table).delete().eq('id', self.getfirstbot().data[0]['id']).execute()

    def deletelastbot(self):
        print('DELETING LAST...')
        return self.supabase.table(self.table).delete().eq('id', self.getlastbot().data[0]['id']).execute()

if __name__ == '__main__':
    botbase = BotBase()
    print(botbase.find())
    print(botbase.getfirstbot())
    print(botbase.getlastbot())

