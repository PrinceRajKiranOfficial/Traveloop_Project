"""Seed script: adds 30 popular Indian travel destinations with activities."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app import create_app
from app.models import db, City, Activity

app = create_app()

INDIAN_CITIES = [
    {"name":"Agra","country":"India","region":"North India","cost_index":1.5,"popularity_score":98,"description":"Home to the iconic Taj Mahal, a UNESCO World Heritage Site and one of the Seven Wonders of the World.","timezone":"Asia/Kolkata"},
    {"name":"Jaipur","country":"India","region":"North India","cost_index":1.8,"popularity_score":96,"description":"The Pink City – majestic forts, vibrant bazaars, and royal Rajasthani heritage.","timezone":"Asia/Kolkata"},
    {"name":"Varanasi","country":"India","region":"North India","cost_index":1.2,"popularity_score":95,"description":"One of the oldest living cities in the world. Sacred ghats along the Ganges and ancient temples.","timezone":"Asia/Kolkata"},
    {"name":"Delhi","country":"India","region":"North India","cost_index":2.0,"popularity_score":97,"description":"India's capital – a blend of Mughal heritage, street food paradise, and modern landmarks.","timezone":"Asia/Kolkata"},
    {"name":"Mumbai","country":"India","region":"West India","cost_index":2.5,"popularity_score":96,"description":"City of Dreams – Gateway of India, Bollywood, street food, and Marine Drive sunsets.","timezone":"Asia/Kolkata"},
    {"name":"Udaipur","country":"India","region":"North India","cost_index":1.8,"popularity_score":94,"description":"City of Lakes – romantic palaces floating on shimmering lakes in Rajasthan.","timezone":"Asia/Kolkata"},
    {"name":"Goa","country":"India","region":"West India","cost_index":2.0,"popularity_score":95,"description":"Sun-kissed beaches, Portuguese heritage churches, vibrant nightlife, and seafood.","timezone":"Asia/Kolkata"},
    {"name":"Kerala Backwaters","country":"India","region":"South India","cost_index":1.8,"popularity_score":94,"description":"Serene backwater cruises on traditional houseboats through lush coconut groves.","timezone":"Asia/Kolkata"},
    {"name":"Rishikesh","country":"India","region":"North India","cost_index":1.3,"popularity_score":90,"description":"Yoga Capital of the World – adventure sports, ashrams, and Ganga Aarti at sunset.","timezone":"Asia/Kolkata"},
    {"name":"Leh-Ladakh","country":"India","region":"North India","cost_index":2.2,"popularity_score":93,"description":"Breathtaking high-altitude desert with Pangong Lake, monasteries, and mountain passes.","timezone":"Asia/Kolkata"},
    {"name":"Hampi","country":"India","region":"South India","cost_index":1.0,"popularity_score":89,"description":"UNESCO ruins of the Vijayanagara Empire – boulder-strewn landscape with ancient temples.","timezone":"Asia/Kolkata"},
    {"name":"Mysore","country":"India","region":"South India","cost_index":1.3,"popularity_score":88,"description":"City of Palaces – the illuminated Mysore Palace, Chamundi Hills, and silk sarees.","timezone":"Asia/Kolkata"},
    {"name":"Darjeeling","country":"India","region":"East India","cost_index":1.5,"popularity_score":87,"description":"Queen of the Hills – tea gardens, toy train, and stunning views of Kanchenjunga.","timezone":"Asia/Kolkata"},
    {"name":"Amritsar","country":"India","region":"North India","cost_index":1.3,"popularity_score":91,"description":"The Golden Temple, Wagah Border ceremony, and legendary Amritsari kulcha.","timezone":"Asia/Kolkata"},
    {"name":"Jodhpur","country":"India","region":"North India","cost_index":1.5,"popularity_score":89,"description":"The Blue City – mighty Mehrangarh Fort towering over a sea of blue houses.","timezone":"Asia/Kolkata"},
    {"name":"Khajuraho","country":"India","region":"Central India","cost_index":1.0,"popularity_score":85,"description":"UNESCO World Heritage temples famous for stunning erotic sculptures and Chandela architecture.","timezone":"Asia/Kolkata"},
    {"name":"Manali","country":"India","region":"North India","cost_index":1.5,"popularity_score":90,"description":"Himalayan hill station – snow peaks, Solang Valley adventures, and Old Manali cafes.","timezone":"Asia/Kolkata"},
    {"name":"Jaisalmer","country":"India","region":"North India","cost_index":1.5,"popularity_score":88,"description":"The Golden City – a living sand-castle fort rising from the Thar Desert.","timezone":"Asia/Kolkata"},
    {"name":"Pondicherry","country":"India","region":"South India","cost_index":1.5,"popularity_score":86,"description":"French Quarter charm, Auroville, pristine beaches, and Tamil-French fusion cuisine.","timezone":"Asia/Kolkata"},
    {"name":"Shimla","country":"India","region":"North India","cost_index":1.8,"popularity_score":87,"description":"Former British summer capital – colonial architecture, Mall Road, and pine forests.","timezone":"Asia/Kolkata"},
    {"name":"Kolkata","country":"India","region":"East India","cost_index":1.5,"popularity_score":88,"description":"City of Joy – Victoria Memorial, Howrah Bridge, street food, and cultural heritage.","timezone":"Asia/Kolkata"},
    {"name":"Hyderabad","country":"India","region":"South India","cost_index":1.8,"popularity_score":89,"description":"City of Pearls – Charminar, Golconda Fort, and legendary Hyderabadi biryani.","timezone":"Asia/Kolkata"},
    {"name":"Chennai","country":"India","region":"South India","cost_index":1.5,"popularity_score":85,"description":"Gateway to South India – ancient temples, Marina Beach, and Chettinad cuisine.","timezone":"Asia/Kolkata"},
    {"name":"Bangalore","country":"India","region":"South India","cost_index":2.0,"popularity_score":86,"description":"Garden City and India's tech hub – craft breweries, parks, and vibrant nightlife.","timezone":"Asia/Kolkata"},
    {"name":"Ranthambore","country":"India","region":"North India","cost_index":2.0,"popularity_score":86,"description":"One of India's best tiger reserves – wildlife safaris amid ancient fort ruins.","timezone":"Asia/Kolkata"},
    {"name":"Andaman Islands","country":"India","region":"Islands","cost_index":2.5,"popularity_score":90,"description":"Turquoise waters, coral reefs, pristine beaches, and Cellular Jail heritage.","timezone":"Asia/Kolkata"},
    {"name":"Munnar","country":"India","region":"South India","cost_index":1.5,"popularity_score":88,"description":"Rolling tea plantations, misty mountains, and Neelakurinji blooms in Kerala.","timezone":"Asia/Kolkata"},
    {"name":"Ajanta & Ellora","country":"India","region":"West India","cost_index":1.2,"popularity_score":87,"description":"UNESCO rock-cut cave temples with exquisite Buddhist, Hindu, and Jain art spanning centuries.","timezone":"Asia/Kolkata"},
    {"name":"Pushkar","country":"India","region":"North India","cost_index":1.0,"popularity_score":84,"description":"Sacred lake town with the only Brahma Temple, famous camel fair, and desert charm.","timezone":"Asia/Kolkata"},
    {"name":"Ooty","country":"India","region":"South India","cost_index":1.5,"popularity_score":85,"description":"Queen of Hill Stations – Nilgiri toy train, botanical gardens, and tea estates.","timezone":"Asia/Kolkata"},
    {"name":"Kaziranga","country":"India","region":"East India","cost_index":1.8,"popularity_score":84,"description":"UNESCO World Heritage site – home to two-thirds of the world's one-horned rhinoceros.","timezone":"Asia/Kolkata"},
    {"name":"Varanasi","country":"India","region":"North India","cost_index":1.2,"popularity_score":95,"description":"Spiritual capital – ancient ghats, Ganga Aarti, silk weaving, and timeless traditions.","timezone":"Asia/Kolkata"},
]

INDIAN_ACTIVITIES = {
    "Agra":[
        {"name":"Taj Mahal Sunrise Visit","category":"sightseeing","cost":50,"duration_hours":3,"rating":4.9,"description":"Watch the marble masterpiece glow at dawn. UNESCO World Heritage Site."},
        {"name":"Agra Fort Tour","category":"culture","cost":35,"duration_hours":2,"rating":4.7,"description":"Mughal red sandstone fortress with stunning views of the Taj Mahal."},
        {"name":"Mehtab Bagh Sunset","category":"sightseeing","cost":25,"duration_hours":1.5,"rating":4.6,"description":"Moonlight Garden across the Yamuna – best sunset view of Taj Mahal."},
        {"name":"Petha & Street Food Walk","category":"food","cost":15,"duration_hours":2,"rating":4.5,"description":"Taste Agra's famous petha sweets and chaat in the old city lanes."},
    ],
    "Jaipur":[
        {"name":"Amber Fort & Elephant Ride","category":"sightseeing","cost":100,"duration_hours":3,"rating":4.8,"description":"Majestic hilltop fortress with mirror palace and panoramic views."},
        {"name":"Hawa Mahal Photo Walk","category":"culture","cost":50,"duration_hours":1.5,"rating":4.7,"description":"Iconic Palace of Winds with 953 honeycomb windows in pink sandstone."},
        {"name":"City Palace Museum","category":"culture","cost":70,"duration_hours":2,"rating":4.6,"description":"Royal residence with textiles, arms gallery, and Peacock Gate."},
        {"name":"Jaipur Bazaar Shopping","category":"shopping","cost":0,"duration_hours":3,"rating":4.5,"description":"Block-printed textiles, gemstones, and blue pottery in Johari Bazaar."},
        {"name":"Rajasthani Thali Dinner","category":"food","cost":40,"duration_hours":2,"rating":4.8,"description":"Traditional dal-baati-churma feast with folk music and dance."},
    ],
    "Varanasi":[
        {"name":"Ganga Aarti at Dashashwamedh","category":"culture","cost":0,"duration_hours":1.5,"rating":4.9,"description":"Mesmerizing evening fire ritual on the sacred ghats of the Ganges."},
        {"name":"Sunrise Boat Ride on Ganges","category":"sightseeing","cost":20,"duration_hours":1.5,"rating":4.8,"description":"Glide past ancient ghats as the sun rises over the holy river."},
        {"name":"Sarnath Buddhist Tour","category":"culture","cost":25,"duration_hours":3,"rating":4.6,"description":"Where Buddha gave his first sermon – ancient stupas and museum."},
        {"name":"Banarasi Street Food Trail","category":"food","cost":15,"duration_hours":2,"rating":4.7,"description":"Kachori, lassi, chaat, and the famous Banarasi paan."},
    ],
    "Delhi":[
        {"name":"Red Fort & Old Delhi Walk","category":"culture","cost":35,"duration_hours":3,"rating":4.7,"description":"Mughal emperor's residence and Chandni Chowk heritage walk."},
        {"name":"Qutub Minar Complex","category":"sightseeing","cost":30,"duration_hours":2,"rating":4.6,"description":"73-metre victory tower – India's tallest brick minaret, UNESCO site."},
        {"name":"Humayun's Tomb","category":"culture","cost":30,"duration_hours":1.5,"rating":4.7,"description":"Precursor to the Taj Mahal – stunning Mughal garden tomb."},
        {"name":"Paranthe Wali Gali Food Tour","category":"food","cost":20,"duration_hours":2,"rating":4.8,"description":"Legendary stuffed paratha lane in Old Delhi with 100+ varieties."},
        {"name":"India Gate & Rajpath","category":"sightseeing","cost":0,"duration_hours":1.5,"rating":4.5,"description":"War memorial and ceremonial boulevard – iconic Delhi landmark."},
    ],
    "Mumbai":[
        {"name":"Gateway of India & Colaba","category":"sightseeing","cost":0,"duration_hours":2,"rating":4.7,"description":"Iconic waterfront arch and the bustling Colaba Causeway market."},
        {"name":"Elephanta Caves Ferry","category":"culture","cost":50,"duration_hours":4,"rating":4.6,"description":"UNESCO rock-cut cave temples on an island in Mumbai Harbour."},
        {"name":"Mumbai Street Food Tour","category":"food","cost":25,"duration_hours":3,"rating":4.9,"description":"Vada pav, pav bhaji, bhel puri – the city's legendary street eats."},
        {"name":"Marine Drive Sunset Walk","category":"sightseeing","cost":0,"duration_hours":1.5,"rating":4.7,"description":"Queen's Necklace promenade curving along the Arabian Sea."},
    ],
    "Udaipur":[
        {"name":"Lake Pichola Boat Cruise","category":"sightseeing","cost":40,"duration_hours":1.5,"rating":4.8,"description":"Sunset cruise past the Lake Palace and Jag Mandir on serene waters."},
        {"name":"City Palace Udaipur","category":"culture","cost":75,"duration_hours":2.5,"rating":4.7,"description":"Largest palace complex in Rajasthan with lake and city views."},
        {"name":"Rajasthani Cooking Class","category":"food","cost":80,"duration_hours":3,"rating":4.8,"description":"Learn to make gatte ki sabzi and laal maas with a local family."},
    ],
    "Goa":[
        {"name":"Old Goa Churches Tour","category":"culture","cost":0,"duration_hours":2.5,"rating":4.6,"description":"Basilica of Bom Jesus and Se Cathedral – UNESCO Portuguese heritage."},
        {"name":"Dudhsagar Waterfalls Trek","category":"adventure","cost":80,"duration_hours":6,"rating":4.7,"description":"Four-tiered waterfall in the Western Ghats – one of India's tallest."},
        {"name":"Beach Hopping & Water Sports","category":"adventure","cost":60,"duration_hours":5,"rating":4.5,"description":"Parasailing, jet ski, and banana rides at Baga and Calangute beaches."},
        {"name":"Goan Seafood Shack Dinner","category":"food","cost":30,"duration_hours":2,"rating":4.8,"description":"Fresh catch with Goan fish curry, prawn balchão, and feni."},
    ],
    "Kerala Backwaters":[
        {"name":"Alleppey Houseboat Cruise","category":"sightseeing","cost":300,"duration_hours":24,"rating":4.9,"description":"Overnight stay on a traditional kettuvallam through palm-fringed canals."},
        {"name":"Kathakali Dance Performance","category":"culture","cost":30,"duration_hours":2,"rating":4.7,"description":"Classical Kerala dance-drama with elaborate costumes and makeup."},
        {"name":"Kerala Sadya Feast","category":"food","cost":25,"duration_hours":1.5,"rating":4.8,"description":"Traditional 26-dish vegetarian feast served on a banana leaf."},
    ],
    "Rishikesh":[
        {"name":"River Rafting on Ganges","category":"adventure","cost":60,"duration_hours":3,"rating":4.8,"description":"Grade III-IV rapids through stunning Himalayan river gorges."},
        {"name":"Bungee Jumping","category":"adventure","cost":300,"duration_hours":1,"rating":4.7,"description":"India's highest bungee at 83 metres over a rocky river gorge."},
        {"name":"Yoga & Meditation Session","category":"culture","cost":20,"duration_hours":2,"rating":4.6,"description":"Traditional yoga at an ashram on the banks of the Ganges."},
        {"name":"Triveni Ghat Aarti","category":"culture","cost":0,"duration_hours":1,"rating":4.7,"description":"Evening prayer ceremony where three sacred rivers meet."},
    ],
    "Leh-Ladakh":[
        {"name":"Pangong Lake Day Trip","category":"nature","cost":150,"duration_hours":10,"rating":4.9,"description":"Crystal-blue high-altitude lake at 4,350m – surreal colour-changing waters."},
        {"name":"Nubra Valley & Camel Safari","category":"adventure","cost":200,"duration_hours":12,"rating":4.8,"description":"Double-humped Bactrian camels in the cold desert via Khardung La pass."},
        {"name":"Thiksey Monastery Visit","category":"culture","cost":10,"duration_hours":2,"rating":4.7,"description":"12-storey Tibetan Buddhist monastery resembling the Potala Palace."},
    ],
    "Hampi":[
        {"name":"Virupaksha Temple","category":"culture","cost":10,"duration_hours":1.5,"rating":4.7,"description":"Active 7th-century temple dedicated to Lord Shiva in the ruins."},
        {"name":"Hampi Boulder Exploration","category":"adventure","cost":0,"duration_hours":3,"rating":4.6,"description":"Scramble over surreal boulder landscapes and discover hidden temples."},
        {"name":"Coracle Ride on Tungabhadra","category":"adventure","cost":15,"duration_hours":1,"rating":4.5,"description":"Traditional round-boat ride across the river to the hippie island."},
    ],
    "Amritsar":[
        {"name":"Golden Temple Visit","category":"culture","cost":0,"duration_hours":3,"rating":4.9,"description":"The holiest Sikh shrine – stunning gold-plated temple and community kitchen."},
        {"name":"Wagah Border Ceremony","category":"culture","cost":0,"duration_hours":2,"rating":4.7,"description":"Electrifying flag-lowering ceremony at the India-Pakistan border."},
        {"name":"Amritsari Food Tour","category":"food","cost":20,"duration_hours":2.5,"rating":4.8,"description":"Kulcha at Bharawan Da Dhaba and lassi at Ahuja Milk Bhandar."},
    ],
    "Jodhpur":[
        {"name":"Mehrangarh Fort Tour","category":"sightseeing","cost":60,"duration_hours":3,"rating":4.9,"description":"One of India's largest forts – museum, ramparts, and blue city views."},
        {"name":"Blue City Heritage Walk","category":"culture","cost":30,"duration_hours":2.5,"rating":4.7,"description":"Wander through the maze of indigo-painted houses in the old town."},
        {"name":"Zip-lining over Mehrangarh","category":"adventure","cost":150,"duration_hours":1.5,"rating":4.6,"description":"Six zip lines flying over the fort walls and desert landscape."},
    ],
    "Manali":[
        {"name":"Solang Valley Adventures","category":"adventure","cost":80,"duration_hours":5,"rating":4.7,"description":"Paragliding, zorbing, and skiing with Himalayan snow peaks."},
        {"name":"Rohtang Pass Day Trip","category":"nature","cost":100,"duration_hours":8,"rating":4.6,"description":"High mountain pass at 3,978m with snow activities and views."},
        {"name":"Old Manali Cafe Hopping","category":"food","cost":20,"duration_hours":3,"rating":4.5,"description":"Cozy Himalayan cafes with Israeli, Italian, and local Kullu cuisine."},
    ],
    "Mysore":[
        {"name":"Mysore Palace Night Visit","category":"sightseeing","cost":40,"duration_hours":2,"rating":4.8,"description":"Indo-Saracenic palace illuminated by 100,000 bulbs on Sunday evenings."},
        {"name":"Chamundi Hills Hike","category":"nature","cost":0,"duration_hours":2,"rating":4.5,"description":"1,000 steps to the hilltop temple with city panorama and Nandi bull."},
        {"name":"Mysore Dosa Breakfast","category":"food","cost":10,"duration_hours":1,"rating":4.7,"description":"Legendary Mysore masala dosa at Mylari or RRR restaurant."},
    ],
    "Darjeeling":[
        {"name":"Toy Train Heritage Ride","category":"sightseeing","cost":50,"duration_hours":2,"rating":4.8,"description":"UNESCO Darjeeling Himalayan Railway through misty tea gardens."},
        {"name":"Tiger Hill Sunrise","category":"nature","cost":20,"duration_hours":3,"rating":4.7,"description":"Spectacular dawn view of Kanchenjunga, the world's third highest peak."},
        {"name":"Tea Estate Tour & Tasting","category":"food","cost":30,"duration_hours":2,"rating":4.6,"description":"Walk through Happy Valley tea estate and taste first-flush Darjeeling."},
    ],
    "Andaman Islands":[
        {"name":"Radhanagar Beach Day","category":"nature","cost":0,"duration_hours":4,"rating":4.9,"description":"Asia's best beach – pristine white sand and turquoise Andaman Sea."},
        {"name":"Scuba Diving at Havelock","category":"adventure","cost":400,"duration_hours":3,"rating":4.8,"description":"Vibrant coral reefs and tropical fish in crystal-clear waters."},
        {"name":"Cellular Jail Light Show","category":"culture","cost":25,"duration_hours":2,"rating":4.6,"description":"Moving sound-and-light show about India's freedom struggle."},
    ],
    "Hyderabad":[
        {"name":"Charminar & Laad Bazaar","category":"culture","cost":25,"duration_hours":2.5,"rating":4.7,"description":"Iconic 16th-century monument and bangle-shopping bazaar."},
        {"name":"Golconda Fort Sound & Light","category":"culture","cost":30,"duration_hours":3,"rating":4.6,"description":"Medieval fortress with incredible acoustics and evening show."},
        {"name":"Hyderabadi Biryani Trail","category":"food","cost":25,"duration_hours":2,"rating":4.9,"description":"Paradise, Bawarchi, and Shah Ghouse – the holy trinity of biryani."},
    ],
    "Kolkata":[
        {"name":"Victoria Memorial Visit","category":"culture","cost":30,"duration_hours":2,"rating":4.7,"description":"Stunning white marble museum set in manicured Mughal gardens."},
        {"name":"Howrah Bridge & Kumartuli","category":"sightseeing","cost":0,"duration_hours":2.5,"rating":4.5,"description":"Iconic cantilever bridge and artisan quarter of idol makers."},
        {"name":"Kolkata Street Food Crawl","category":"food","cost":15,"duration_hours":2.5,"rating":4.8,"description":"Kathi rolls, phuchka, mishti doi, and rosogolla in the city of joy."},
    ],
}

def seed_india():
    with app.app_context():
        existing = City.query.filter_by(country="India").count()
        if existing >= 30:
            print(f"Already have {existing} Indian cities. Skipping.")
            return

        # Remove duplicate Varanasi from list
        seen = set()
        unique_cities = []
        for c in INDIAN_CITIES:
            if c["name"] not in seen:
                seen.add(c["name"])
                unique_cities.append(c)

        print(f"Seeding {len(unique_cities)} Indian cities...")
        city_map = {}
        for c in unique_cities:
            city = City(**c)
            db.session.add(city)
            db.session.flush()
            city_map[c["name"]] = city

        act_count = 0
        for city_name, acts in INDIAN_ACTIVITIES.items():
            city = city_map.get(city_name)
            if not city:
                continue
            for a in acts:
                db.session.add(Activity(city_id=city.id, **a))
                act_count += 1

        db.session.commit()
        print(f"[OK] Seeded {len(unique_cities)} Indian cities and {act_count} activities.")

if __name__ == "__main__":
    seed_india()
