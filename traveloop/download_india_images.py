import os
import sys
import urllib.request
import urllib.parse
import json
import time

CITIES_DIR = os.path.join(os.path.dirname(__file__), "app", "static", "cities")
os.makedirs(CITIES_DIR, exist_ok=True)

from seed_india import INDIAN_CITIES

# Some cities might need better search terms for Wikipedia
WIKI_SEARCH_TERMS = {
    "Kerala Backwaters": "Kerala backwaters",
    "Leh-Ladakh": "Ladakh",
    "Ranthambore": "Ranthambore National Park",
    "Andaman Islands": "Andaman Islands",
    "Ajanta & Ellora": "Ellora Caves",
    "Kaziranga": "Kaziranga National Park"
}

headers = {
    "User-Agent": "TraveloopApp/1.0 (contact@traveloop.com)"
}

def get_wiki_image(city_query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(city_query)}&prop=pageimages&format=json&pithumbsize=800"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            pages = data['query']['pages']
            for page_id in pages:
                if page_id == "-1": continue
                if 'thumbnail' in pages[page_id]:
                    return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching wiki info for {city_query}: {e}")
    return None

def download(filename, url):
    dest = os.path.join(CITIES_DIR, filename)
    if os.path.exists(dest):
        print(f"  [SKIP] {filename} already exists")
        return True
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  [OK]   {filename} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL] {filename}: {e}")
        return False

print("Downloading Indian city images from Wikipedia...")
seen = set()
for c_dict in INDIAN_CITIES:
    city_name = c_dict["name"]
    if city_name in seen:
        continue
    seen.add(city_name)
    
    query = WIKI_SEARCH_TERMS.get(city_name, city_name)
    img_url = get_wiki_image(query)
    
    filename = city_name.lower().replace(" ", "_").replace("&", "and") + ".jpg"
    
    if img_url:
        download(filename, img_url)
    else:
        print(f"  [FAIL] Could not find image for {city_name}")
    
    time.sleep(0.5)

print("\nAll done!")

print("\nMapping string for Jinja:")
for city_name in seen:
    filename = city_name.lower().replace(" ", "_").replace("&", "and") + ".jpg"
    print(f"    '{city_name}': 'cities/{filename}',")
