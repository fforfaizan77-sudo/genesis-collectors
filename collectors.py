import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random

# --- CONFIG ---
with open("config.json") as f:
    config = json.load(f)

# --- GOOGLE SHEETS SETUP ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(config["google_api_credentials_file"], scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(config["google_sheet_id"]).sheet1

# --- PLACEHOLDER COLLECTORS ---
def collect_reddit():
    return [{"source": "reddit", "topic": "AI Trend " + str(i), "popularity": random.uniform(0, 1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_youtube():
    return [{"source": "youtube", "topic": "Short Video Trend " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_tiktok():
    return [{"source": "tiktok", "topic": "Viral Hashtag " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_amazon():
    return [{"source": "amazon", "topic": "Trending Product " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_etsy():
    return [{"source": "etsy", "topic": "Trending Item " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_google_trends():
    return [{"source": "google_trends", "topic": "Search Spike " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_github():
    return [{"source": "github", "topic": "New Repo " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

def collect_job_boards():
    return [{"source": "job_board", "topic": "Emerging Demand " + str(i), "popularity": random.uniform(0,1), "timestamp": str(datetime.now())} for i in range(3)]

# --- MAIN COLLECTION ---
all_data = []

if config["sources"]["reddit"]:
    all_data += collect_reddit()
if config["sources"]["youtube"]:
    all_data += collect_youtube()
if config["sources"]["tiktok"]:
    all_data += collect_tiktok()
if config["sources"]["amazon"]:
    all_data += collect_amazon()
if config["sources"]["etsy"]:
    all_data += collect_etsy()
if config["sources"]["google_trends"]:
    all_data += collect_google_trends()
if config["sources"]["github"]:
    all_data += collect_github()
if config["sources"]["job_boards"]:
    all_data += collect_job_boards()

# --- FILTER BY PRIORITY ---
high_priority = [d for d in all_data if d["popularity"] >= config["priority_threshold"]]

# --- WRITE TO SHEET ---
for item in high_priority:
    sheet.append_row([item["timestamp"], item["source"], item["topic"], item["popularity"]])

print(f"Genesis scanned {len(all_data)} items. {len(high_priority)} high-priority items saved.")
