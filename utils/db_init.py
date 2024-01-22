import os
from dotenv import load_dotenv, find_dotenv
from supabase import create_client, Client

load_dotenv(find_dotenv())

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

async def insert_data(data: dict, table_name="news_data"):
    supabase.table(table_name).insert(data).execute()

def get_data(table_name: str):
    return supabase.table(table_name).select("*").execute()

def update_data(table_name: str, id: int, data: dict):
    supabase.table(table_name).update(data).where("id", "eq", id).execute()
