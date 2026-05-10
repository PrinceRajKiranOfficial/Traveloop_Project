"""Download high-quality city images from Wikimedia Commons."""
import os
import urllib.request
import time

CITIES_DIR = os.path.join(os.path.dirname(__file__), "app", "static", "cities")
os.makedirs(CITIES_DIR, exist_ok=True)

# Direct Wikimedia Commons image URLs – each is a famous, iconic photo of the city
CITY_IMAGES = {
    "paris": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/320px-New_york_times_square-terabass.jpg",
    "tokyo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/640px-Skyscrapers_of_Shinjuku_2009_January.jpg",
    "new_york": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/640px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
    "bali": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Bali_Indonesia_%2817%29.jpg/640px-Bali_Indonesia_%2817%29.jpg",
    "rome": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/640px-Colosseo_2020.jpg",
    "bangkok": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Wat_Arun_at_dusk_2.jpg/640px-Wat_Arun_at_dusk_2.jpg",
    "barcelona": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg",
    "cape_town": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/24701-nature-natural-beauty.jpg/640px-24701-nature-natural-beauty.jpg",
    "dubai": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Burj_Khalifa_building.jpg/640px-Burj_Khalifa_building.jpg",
    "sydney": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Sydney_Harbor_Bridge_New_Year%27s_2009.jpg/640px-Sydney_Harbor_Bridge_New_Year%27s_2009.jpg",
    "santorini": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Thira.jpg/640px-Thira.jpg",
    "kyoto": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Fushimi_Inari_Taisha_%281%29.jpg/640px-Fushimi_Inari_Taisha_%281%29.jpg",
    "marrakech": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Jemaa_el-Fnaa_at_night.jpg/640px-Jemaa_el-Fnaa_at_night.jpg",
    "prague": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_night_view_of_Prague.jpg/640px-A_night_view_of_Prague.jpg",
    "rio": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Cristo_Redentor_-_Rio_de_Janeiro%2C_Brasil.jpg/640px-Cristo_Redentor_-_Rio_de_Janeiro%2C_Brasil.jpg",
    "amsterdam": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Amsterdamse_grachten%2C_Amsterdam.jpg/640px-Amsterdamse_grachten%2C_Amsterdam.jpg",
    "singapore": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Gardens_by_the_Bay%2C_Singapore%2C_2013-06-01.jpg/640px-Gardens_by_the_Bay%2C_Singapore%2C_2013-06-01.jpg",
    "istanbul": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Hagia_Sophia_Mars_2013.jpg/640px-Hagia_Sophia_Mars_2013.jpg",
    "lisbon": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Lisbon_Lisboa_Portugal_October_2017.jpg/640px-Lisbon_Lisboa_Portugal_October_2017.jpg",
    "mexico_city": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Teotihuacan_Pyramid_of_the_Sun_1.jpg/640px-Teotihuacan_Pyramid_of_the_Sun_1.jpg",
}

# Better, more reliable Unsplash static image URLs (no API key needed for source.unsplash.com)
CITY_IMAGES_UNSPLASH = {
    "paris":       "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
    "tokyo":       "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80",
    "new_york":    "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800&q=80",
    "bali":        "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80",
    "rome":        "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80",
    "bangkok":     "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=800&q=80",
    "barcelona":   "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800&q=80",
    "cape_town":   "https://images.unsplash.com/photo-1580060839134-75a5edca2e99?w=800&q=80",
    "dubai":       "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80",
    "sydney":      "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800&q=80",
    "santorini":   "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=800&q=80",
    "kyoto":       "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800&q=80",
    "marrakech":   "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?w=800&q=80",
    "prague":      "https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=800&q=80",
    "rio":         "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800&q=80",
    "amsterdam":   "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800&q=80",
    "singapore":   "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&q=80",
    "istanbul":    "https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?w=800&q=80",
    "lisbon":      "https://images.unsplash.com/photo-1548707309-dcebeab9ea9b?w=800&q=80",
    "mexico_city": "https://images.unsplash.com/photo-1518659526054-190340b32735?w=800&q=80",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download(city_key, url, filename):
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

print("Downloading city images from Unsplash...")
for key, url in CITY_IMAGES_UNSPLASH.items():
    download(key, url, f"{key}.jpg")
    time.sleep(0.3)

print("\nAll done! Images saved to:", CITIES_DIR)

# Print mapping for template use
print("\nCity → filename mapping:")
city_name_map = {
    "Paris": "paris", "Tokyo": "tokyo", "New York": "new_york",
    "Bali": "bali", "Rome": "rome", "Bangkok": "bangkok",
    "Barcelona": "barcelona", "Cape Town": "cape_town", "Dubai": "dubai",
    "Sydney": "sydney", "Santorini": "santorini", "Kyoto": "kyoto",
    "Marrakech": "marrakech", "Prague": "prague", "Rio de Janeiro": "rio",
    "Amsterdam": "amsterdam", "Singapore": "singapore", "Istanbul": "istanbul",
    "Lisbon": "lisbon", "Mexico City": "mexico_city",
}
for name, key in city_name_map.items():
    print(f'  "{name}": "cities/{key}.jpg"')
