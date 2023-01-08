from dotenv import load_dotenv
import os
from supabase import create_client, Client

from bot import Bot

load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
table = os.getenv('SUPABASE_TABLE')
print(url, key)
supabase: Client = create_client(url, key)


def find() -> dict:
    data = supabase.table(table).select("*").execute()
    # Equivalent for SQL Query "SELECT * FROM teamsTest;"
    if data != 0: return data
    else: return None

def insert(data):
    print('INSETING...')
    return supabase.table(table).insert(data).execute()

def delete(id):
    print('DELETING...')
    return supabase.table(table).delete().eq('id', id).execute()

teams = find() # Fetch all data
print(teams.data)
