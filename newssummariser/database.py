import requests
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def save_article(title, summary):
    url = f"{SUPABASE_URL}/rest/v1/saved_articles"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": title,
        "summary": summary
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        return True
    else:
        print("Save failed:", response.text)
        return False

def get_saved_articles():
    url = f"{SUPABASE_URL}/rest/v1/saved_articles?select=*&order=saved_at.desc"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []