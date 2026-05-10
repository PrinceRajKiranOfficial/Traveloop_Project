"""Seed script: populates cities, activities, and a demo user."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app.models import db, User, City, Activity

app = create_app()

CITIES = [
    {"name": "Paris", "country": "France", "region": "Europe", "cost_index": 4.0, "popularity_score": 98, "description": "The City of Light, famous for the Eiffel Tower, world-class cuisine, and art museums."},
    {"name": "Tokyo", "country": "Japan", "region": "Asia", "cost_index": 3.5, "popularity_score": 97, "description": "A vibrant metropolis blending ultramodern and traditional, from neon-lit skyscrapers to historic temples."},
    {"name": "New York", "country": "USA", "region": "North America", "cost_index": 4.5, "popularity_score": 96, "description": "The Big Apple – iconic skyline, Broadway shows, Central Park, and world-famous food."},
    {"name": "Bali", "country": "Indonesia", "region": "Asia", "cost_index": 1.5, "popularity_score": 94, "description": "Tropical paradise with lush rice terraces, surf beaches, and sacred Hindu temples."},
    {"name": "Rome", "country": "Italy", "region": "Europe", "cost_index": 3.2, "popularity_score": 93, "description": "The Eternal City – Colosseum, Vatican, and incomparable pasta and gelato."},
    {"name": "Bangkok", "country": "Thailand", "region": "Asia", "cost_index": 1.8, "popularity_score": 92, "description": "Street food paradise with ornate shrines, vibrant nightlife, and floating markets."},
    {"name": "Barcelona", "country": "Spain", "region": "Europe", "cost_index": 3.0, "popularity_score": 91, "description": "Gaudí architecture, sunny beaches, and legendary tapas culture on the Mediterranean."},
    {"name": "Cape Town", "country": "South Africa", "region": "Africa", "cost_index": 2.0, "popularity_score": 89, "description": "Stunning Table Mountain backdrop with winelands, beaches, and rich cultural heritage."},
    {"name": "Dubai", "country": "UAE", "region": "Middle East", "cost_index": 4.2, "popularity_score": 88, "description": "Futuristic skyline, luxury shopping, and desert adventures in one glittering city."},
    {"name": "Sydney", "country": "Australia", "region": "Oceania", "cost_index": 4.0, "popularity_score": 87, "description": "Iconic Opera House, Bondi Beach, and the world's most beautiful harbour."},
    {"name": "Santorini", "country": "Greece", "region": "Europe", "cost_index": 3.8, "popularity_score": 90, "description": "White-washed cliffs, blue-domed churches, and breathtaking Aegean sunsets."},
    {"name": "Kyoto", "country": "Japan", "region": "Asia", "cost_index": 3.0, "popularity_score": 86, "description": "Japan's cultural heart – bamboo groves, geisha districts, and a thousand temples."},
    {"name": "Marrakech", "country": "Morocco", "region": "Africa", "cost_index": 1.6, "popularity_score": 85, "description": "Labyrinthine medina, vibrant souks, and the magical Djemaa el-Fna square."},
    {"name": "Prague", "country": "Czech Republic", "region": "Europe", "cost_index": 2.5, "popularity_score": 84, "description": "Fairytale old town, medieval castle, and affordable beer in the heart of Europe."},
    {"name": "Rio de Janeiro", "country": "Brazil", "region": "South America", "cost_index": 2.8, "popularity_score": 83, "description": "Carnival, Christ the Redeemer, Copacabana, and samba in the Marvelous City."},
    {"name": "Amsterdam", "country": "Netherlands", "region": "Europe", "cost_index": 3.5, "popularity_score": 82, "description": "Picturesque canals, world-class museums, and a free-spirited culture."},
    {"name": "Singapore", "country": "Singapore", "region": "Asia", "cost_index": 4.0, "popularity_score": 81, "description": "A clean, green city-state of futuristic gardens, hawker food, and Marina Bay Sands."},
    {"name": "Istanbul", "country": "Turkey", "region": "Europe/Asia", "cost_index": 2.2, "popularity_score": 80, "description": "Where East meets West – Hagia Sophia, Grand Bazaar, and bosphorus sunsets."},
    {"name": "Lisbon", "country": "Portugal", "region": "Europe", "cost_index": 2.8, "popularity_score": 79, "description": "Hilly city of trams, Fado music, pastéis de nata, and stunning azulejo tiles."},
    {"name": "Mexico City", "country": "Mexico", "region": "North America", "cost_index": 1.9, "popularity_score": 78, "description": "Ancient Aztec ruins beneath a vibrant megalopolis of tacos, art, and culture."},
]

ACTIVITIES = {
    "Paris": [
        {"name": "Eiffel Tower Visit", "category": "sightseeing", "cost": 28, "duration_hours": 2.5, "rating": 4.8, "description": "Skip-the-line tickets to the iconic iron tower. Best at sunset."},
        {"name": "Louvre Museum", "category": "culture", "cost": 22, "duration_hours": 4, "rating": 4.7, "description": "World's largest art museum – home to the Mona Lisa and Venus de Milo."},
        {"name": "Seine River Cruise", "category": "sightseeing", "cost": 18, "duration_hours": 1.5, "rating": 4.5, "description": "Romantic 1-hour cruise past Notre-Dame, Eiffel Tower, and bridges."},
        {"name": "Montmartre & Sacré-Cœur", "category": "culture", "cost": 0, "duration_hours": 3, "rating": 4.6, "description": "Bohemian hilltop village with the gleaming white basilica and artist squares."},
        {"name": "French Cooking Class", "category": "food", "cost": 95, "duration_hours": 3, "rating": 4.9, "description": "Learn to make croissants and coq au vin with a local chef."},
    ],
    "Tokyo": [
        {"name": "Shinjuku Gyoen Garden", "category": "nature", "cost": 5, "duration_hours": 2, "rating": 4.6, "description": "Stunning blend of Japanese and French garden styles – cherry blossoms in spring."},
        {"name": "Tsukiji Outer Market Food Tour", "category": "food", "cost": 35, "duration_hours": 2, "rating": 4.8, "description": "Fresh sushi, tamagoyaki, and street snacks at the famous fish market."},
        {"name": "Akihabara Electronics Tour", "category": "shopping", "cost": 0, "duration_hours": 3, "rating": 4.4, "description": "Anime, manga, and gadgets galore in Tokyo's electric town."},
        {"name": "teamLab Borderless", "category": "culture", "cost": 38, "duration_hours": 2.5, "rating": 4.9, "description": "Immersive digital art museum unlike anything else in the world."},
        {"name": "Fuji Day Trip", "category": "adventure", "cost": 70, "duration_hours": 10, "rating": 4.7, "description": "Guided day trip to Mount Fuji and the Fuji Five Lakes region."},
    ],
    "New York": [
        {"name": "Central Park Walk", "category": "nature", "cost": 0, "duration_hours": 3, "rating": 4.7, "description": "843-acre urban oasis with the Bethesda Fountain, Bow Bridge, and Sheep Meadow."},
        {"name": "Metropolitan Museum of Art", "category": "culture", "cost": 30, "duration_hours": 4, "rating": 4.8, "description": "One of the world's great art museums spanning 5,000 years of history."},
        {"name": "Broadway Show", "category": "culture", "cost": 120, "duration_hours": 3, "rating": 4.9, "description": "A world-class theatrical experience in the Theater District of Midtown Manhattan."},
        {"name": "Brooklyn Bridge Walk", "category": "sightseeing", "cost": 0, "duration_hours": 1.5, "rating": 4.6, "description": "Iconic pedestrian walkway with stunning Manhattan skyline views."},
        {"name": "NYC Food Tour – Hell's Kitchen", "category": "food", "cost": 65, "duration_hours": 3, "rating": 4.7, "description": "Sample diverse cuisines of the melting-pot neighborhood on the West Side."},
    ],
    "Bali": [
        {"name": "Ubud Monkey Forest", "category": "nature", "cost": 6, "duration_hours": 2, "rating": 4.4, "description": "Sacred forest sanctuary home to over 700 Balinese long-tailed macaques."},
        {"name": "Tanah Lot Temple at Sunset", "category": "culture", "cost": 4, "duration_hours": 2, "rating": 4.8, "description": "Sea temple perched on a rock formation – one of Bali's most iconic sights."},
        {"name": "Tegallalang Rice Terrace Trek", "category": "adventure", "cost": 3, "duration_hours": 3, "rating": 4.6, "description": "UNESCO-listed cascading rice paddies north of Ubud with café swings."},
        {"name": "Balinese Cooking Class", "category": "food", "cost": 40, "duration_hours": 4, "rating": 4.8, "description": "Market visit and hands-on cooking of satay, nasi goreng, and lawar."},
        {"name": "Surf Lesson – Kuta Beach", "category": "adventure", "cost": 25, "duration_hours": 2, "rating": 4.5, "description": "Beginner-friendly surf school on one of Bali's most famous waves."},
    ],
    "Rome": [
        {"name": "Colosseum & Roman Forum", "category": "sightseeing", "cost": 18, "duration_hours": 3, "rating": 4.8, "description": "Ancient amphitheater that once held 80,000 spectators for gladiatorial combat."},
        {"name": "Vatican Museums & Sistine Chapel", "category": "culture", "cost": 27, "duration_hours": 4, "rating": 4.9, "description": "Michelangelo's breathtaking ceiling and centuries of papal art treasures."},
        {"name": "Pasta Making Class", "category": "food", "cost": 75, "duration_hours": 3, "rating": 4.9, "description": "Hand-roll tagliatelle and ravioli under a Roman chef's expert guidance."},
        {"name": "Trastevere Evening Walk", "category": "nightlife", "cost": 0, "duration_hours": 3, "rating": 4.6, "description": "Wander the cobblestone streets of Rome's most charming medieval neighborhood."},
    ],
    "Bangkok": [
        {"name": "Grand Palace & Wat Phra Kaew", "category": "culture", "cost": 15, "duration_hours": 3, "rating": 4.7, "description": "Dazzling palace complex housing the sacred Emerald Buddha statue."},
        {"name": "Chatuchak Weekend Market", "category": "shopping", "cost": 0, "duration_hours": 4, "rating": 4.5, "description": "One of the world's largest markets – 15,000 stalls of everything imaginable."},
        {"name": "Thai Street Food Tour", "category": "food", "cost": 30, "duration_hours": 3, "rating": 4.8, "description": "Pad Thai, mango sticky rice, and boat noodles with a local food guide."},
        {"name": "Chao Phraya River Cruise", "category": "sightseeing", "cost": 12, "duration_hours": 2, "rating": 4.4, "description": "Sunset dinner cruise past temples and golden pagodas on the river of kings."},
    ],
    "Barcelona": [
        {"name": "Sagrada Família", "category": "sightseeing", "cost": 35, "duration_hours": 2.5, "rating": 4.9, "description": "Gaudí's awe-inspiring unfinished basilica, a UNESCO World Heritage Site."},
        {"name": "Park Güell", "category": "culture", "cost": 14, "duration_hours": 2, "rating": 4.6, "description": "Gaudí's mosaic-covered park with stunning city views."},
        {"name": "La Boqueria Market & Tapas Tour", "category": "food", "cost": 50, "duration_hours": 3, "rating": 4.7, "description": "Explore the famous market then hop tapas bars in the Gothic Quarter."},
        {"name": "Barceloneta Beach Day", "category": "nature", "cost": 0, "duration_hours": 4, "rating": 4.3, "description": "Sandy urban beach on the Mediterranean with beach volleyball and chiringuitos."},
    ],
    "Cape Town": [
        {"name": "Table Mountain Cable Car", "category": "adventure", "cost": 28, "duration_hours": 3, "rating": 4.8, "description": "Revolving cable car to the flat-topped mountain with 360° city views."},
        {"name": "Cape Winelands Tour", "category": "food", "cost": 85, "duration_hours": 8, "rating": 4.7, "description": "Stellenbosch and Franschhoek estates with wine tastings and gourmet lunch."},
        {"name": "Robben Island Tour", "category": "culture", "cost": 22, "duration_hours": 4, "rating": 4.6, "description": "Former prison island where Nelson Mandela was held for 18 years."},
        {"name": "Boulders Beach Penguin Colony", "category": "nature", "cost": 8, "duration_hours": 2, "rating": 4.7, "description": "Walk among African penguins on a beautiful sheltered beach near Simon's Town."},
    ],
    "Dubai": [
        {"name": "Burj Khalifa At the Top", "category": "sightseeing", "cost": 45, "duration_hours": 2, "rating": 4.7, "description": "Observation deck on the world's tallest building – 124th and 125th floors."},
        {"name": "Desert Safari & BBQ Dinner", "category": "adventure", "cost": 65, "duration_hours": 6, "rating": 4.8, "description": "Dune bashing, camel rides, falconry, and a buffet dinner under the stars."},
        {"name": "Dubai Mall & Aquarium", "category": "shopping", "cost": 15, "duration_hours": 4, "rating": 4.5, "description": "The world's largest mall with a 10-million-litre aquarium inside."},
        {"name": "Dubai Creek Dhow Cruise", "category": "sightseeing", "cost": 35, "duration_hours": 2, "rating": 4.4, "description": "Traditional wooden dhow dinner cruise past the glittering Gold Souk."},
    ],
    "Sydney": [
        {"name": "Sydney Opera House Tour", "category": "culture", "cost": 45, "duration_hours": 1.5, "rating": 4.7, "description": "Guided backstage tour of the world's most recognisable performing arts venue."},
        {"name": "Bondi to Coogee Coastal Walk", "category": "nature", "cost": 0, "duration_hours": 3, "rating": 4.8, "description": "Stunning 6km clifftop walk with ocean pools, sea views, and cafés."},
        {"name": "Sydney Harbour Bridge Climb", "category": "adventure", "cost": 175, "duration_hours": 3.5, "rating": 4.9, "description": "Climb to the summit of the Harbour Bridge for unbeatable city panoramas."},
        {"name": "Manly Beach Ferry & Day", "category": "nature", "cost": 12, "duration_hours": 5, "rating": 4.6, "description": "Ferry from Circular Quay to the famous surf beach and village."},
    ],
    "Santorini": [
        {"name": "Oia Sunset Walk", "category": "sightseeing", "cost": 0, "duration_hours": 3, "rating": 4.9, "description": "World-famous sunset views from the iconic blue-domed village of Oia."},
        {"name": "Caldera Sailing Cruise", "category": "adventure", "cost": 85, "duration_hours": 6, "rating": 4.8, "description": "Catamaran around the volcanic caldera with hot springs swim and BBQ."},
        {"name": "Wine Tasting at Santo Winery", "category": "food", "cost": 40, "duration_hours": 2, "rating": 4.7, "description": "Asymtiko wine tasting with caldera views on the highest winery in Santorini."},
    ],
    "Kyoto": [
        {"name": "Fushimi Inari Shrine", "category": "culture", "cost": 0, "duration_hours": 3, "rating": 4.8, "description": "Thousands of torii gates winding up a forested mountain – most iconic in Japan."},
        {"name": "Arashiyama Bamboo Grove", "category": "nature", "cost": 0, "duration_hours": 2, "rating": 4.7, "description": "Towering bamboo stalks create an otherworldly tunnel near Tenryu-ji."},
        {"name": "Tea Ceremony Experience", "category": "culture", "cost": 30, "duration_hours": 1.5, "rating": 4.6, "description": "Traditional matcha tea ceremony in a centuries-old Kyoto machiya."},
        {"name": "Nishiki Market Food Walk", "category": "food", "cost": 0, "duration_hours": 2, "rating": 4.5, "description": "Kyoto's 'Kitchen' – 400-year-old covered market with pickles, tofu, and sweets."},
    ],
    "Marrakech": [
        {"name": "Djemaa el-Fna Square", "category": "culture", "cost": 0, "duration_hours": 3, "rating": 4.7, "description": "UNESCO-listed square transforms at dusk into a carnival of storytellers and food."},
        {"name": "Medina Souk Tour", "category": "shopping", "cost": 0, "duration_hours": 4, "rating": 4.5, "description": "Navigate the labyrinthine souks for spices, leather goods, and Berber rugs."},
        {"name": "Moroccan Cooking Class", "category": "food", "cost": 55, "duration_hours": 4, "rating": 4.8, "description": "Learn to make tagine, couscous, and harira with a local cook in a riad kitchen."},
        {"name": "Atlas Mountains Day Trip", "category": "adventure", "cost": 60, "duration_hours": 9, "rating": 4.6, "description": "Berber villages, Ourika Valley waterfalls, and panoramic mountain views."},
    ],
    "Prague": [
        {"name": "Prague Castle Complex", "category": "sightseeing", "cost": 15, "duration_hours": 3.5, "rating": 4.7, "description": "Largest ancient castle in the world, housing St. Vitus Cathedral and Royal Palace."},
        {"name": "Charles Bridge at Dawn", "category": "sightseeing", "cost": 0, "duration_hours": 1, "rating": 4.8, "description": "Baroque-statue-lined bridge over the Vltava – magical before the crowds arrive."},
        {"name": "Czech Beer & Food Tour", "category": "food", "cost": 45, "duration_hours": 3, "rating": 4.6, "description": "Pilsner Urquell and svíčková in traditional Prague pubs with a local guide."},
    ],
    "Amsterdam": [
        {"name": "Anne Frank House", "category": "culture", "cost": 16, "duration_hours": 2, "rating": 4.8, "description": "The historic hiding place of Anne Frank during World War II – deeply moving."},
        {"name": "Rijksmuseum", "category": "culture", "cost": 22, "duration_hours": 3, "rating": 4.7, "description": "Dutch Golden Age masterworks including Rembrandt's Night Watch."},
        {"name": "Canal Bike Tour", "category": "adventure", "cost": 30, "duration_hours": 2, "rating": 4.5, "description": "Pedal a water bike through Amsterdam's UNESCO-listed canal ring."},
    ],
    "Singapore": [
        {"name": "Gardens by the Bay", "category": "nature", "cost": 28, "duration_hours": 3, "rating": 4.8, "description": "Futuristic Supertrees and climate-controlled biomes with rare flora from around the world."},
        {"name": "Hawker Centre Food Crawl", "category": "food", "cost": 15, "duration_hours": 2, "rating": 4.9, "description": "Maxwell, Lau Pa Sat, Newton – Michelin-starred hawker stalls and local favourites."},
        {"name": "Universal Studios Singapore", "category": "adventure", "cost": 80, "duration_hours": 8, "rating": 4.6, "description": "Southeast Asia's only Universal Studios theme park on Sentosa Island."},
    ],
    "Istanbul": [
        {"name": "Hagia Sophia", "category": "culture", "cost": 0, "duration_hours": 2, "rating": 4.8, "description": "Magnificent 6th-century Byzantine basilica turned mosque with golden mosaics."},
        {"name": "Grand Bazaar", "category": "shopping", "cost": 0, "duration_hours": 3, "rating": 4.6, "description": "One of the oldest and largest covered markets in the world – 4,000 shops."},
        {"name": "Bosphorus Cruise", "category": "sightseeing", "cost": 20, "duration_hours": 2, "rating": 4.7, "description": "Sail between Europe and Asia past palaces, fortresses, and fishing villages."},
    ],
    "Lisbon": [
        {"name": "Belém Tower & Pastéis de Belém", "category": "culture", "cost": 8, "duration_hours": 3, "rating": 4.7, "description": "16th-century fortress on the Tagus river, then taste the original custard tarts."},
        {"name": "Tram 28 Ride", "category": "sightseeing", "cost": 3, "duration_hours": 1, "rating": 4.5, "description": "Iconic yellow tram rattling through Alfama's steep hills and narrow streets."},
        {"name": "Fado Show Dinner", "category": "nightlife", "cost": 55, "duration_hours": 3, "rating": 4.8, "description": "Soulful Portuguese folk music performed live in a traditional Alfama restaurant."},
    ],
    "Rio de Janeiro": [
        {"name": "Christ the Redeemer", "category": "sightseeing", "cost": 30, "duration_hours": 3, "rating": 4.8, "description": "The iconic 38-metre Art Deco statue atop Corcovado Mountain – a New Wonder of the World."},
        {"name": "Copacabana & Ipanema Beach", "category": "nature", "cost": 0, "duration_hours": 4, "rating": 4.6, "description": "World-famous beaches with volleyball, caipirinha vendors, and spectacular sunsets."},
        {"name": "Samba Night at Lapa", "category": "nightlife", "cost": 25, "duration_hours": 4, "rating": 4.7, "description": "Dance samba at the legendary Lapa Arches clubs with live music all night."},
    ],
    "Mexico City": [
        {"name": "Teotihuacán Pyramids", "category": "culture", "cost": 6, "duration_hours": 6, "rating": 4.8, "description": "Climb the Pyramid of the Sun and Moon at the ancient Aztec city northeast of CDMX."},
        {"name": "Frida Kahlo Museum", "category": "culture", "cost": 14, "duration_hours": 2.5, "rating": 4.7, "description": "The iconic Blue House where Frida Kahlo was born, lived, and created her art."},
        {"name": "Street Taco Tour", "category": "food", "cost": 25, "duration_hours": 3, "rating": 4.9, "description": "Al pastor, barbacoa, and quesillo with a local guide through La Merced and Centro."},
    ],
}


def seed():
    with app.app_context():
        # Check if already seeded
        if City.query.count() > 0:
            print("Database already seeded. Skipping.")
            return

        print("Seeding cities...")
        city_map = {}
        for c in CITIES:
            city = City(**c)
            db.session.add(city)
            db.session.flush()
            city_map[c["name"]] = city

        print("Seeding activities...")
        for city_name, acts in ACTIVITIES.items():
            city = city_map.get(city_name)
            if not city:
                continue
            for a in acts:
                act = Activity(city_id=city.id, **a)
                db.session.add(act)

        # Demo user
        if not User.query.filter_by(email="demo@traveloop.com").first():
            print("Creating demo user...")
            demo = User(name="Demo Traveler", email="demo@traveloop.com")
            demo.set_password("demo1234")
            db.session.add(demo)

        db.session.commit()
        print(f"[OK] Seeded {len(CITIES)} cities and {sum(len(v) for v in ACTIVITIES.values())} activities.")
        print("   Demo login: demo@traveloop.com / demo1234")


if __name__ == "__main__":
    seed()
