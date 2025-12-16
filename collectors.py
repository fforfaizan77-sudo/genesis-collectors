import argparse
import gspread
from oauth2client.service_account import ServiceAccountCredentials

parser = argparse.ArgumentParser()
parser.add_argument("--credentials", required=True)
args = parser.parse_args()

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(args.credentials, scope)
client = gspread.authorize(creds)

# --- PLACEHOLDER COLLECTOR FUNCTIONS ---
# These will later be replaced with REAL API calls.
# For now, they generate realistic test data.

def collect_reddit():
    return [{
        "source": "reddit",
        "topic": f"Reddit Trend {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_youtube():
    return [{
        "source": "youtube",
        "topic": f"Youtube Viral {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_tiktok():
    return [{
        "source": "tiktok",
        "topic": f"Tiktok Trend {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_amazon():
    return [{
        "source": "amazon",
        "topic": f"Amazon Trending Product {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_etsy():
    return [{
        "source": "etsy",
        "topic": f"Etsy Trending {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_google_trends():
    return [{
        "source": "google_trends",
        "topic": f"Search Spike {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_github():
    return [{
        "source": "github",
        "topic": f"New AI Repo {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]

def collect_job_boards():
    return [{
        "source": "job_board",
        "topic": f"Emerging Job Demand {i}",
        "popularity": random.uniform(0, 1),
        "timestamp": str(datetime.now())
    } for i in range(5)]


# --- MAIN COLLECTION LOGIC ---
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

# --- PRIORITY FILTER ---
priority = config["priority_threshold"]
high_priority = [item for item in all_data if item["popularity"] >= priority]

# --- WRITE HIGH-PRIORITY RESULTS TO GOOGLE SHEET ---
for item in high_priority:
    sheet.append_row([
        item["timestamp"],
        item["source"],
        item["topic"],
        item["popularity"]
    ])

print(f"Genesis scanned {len(all_data)} items. {len(high_priority)} items saved.")

