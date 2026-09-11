from .models import Destination


DESTINATIONS = [
    Destination("Cancun", "Mexico", "CUN", "warm", 1750, True, ("beach", "food", "culture", "relaxation"), "A bright Caribbean escape with calm water, historic neighborhoods, and easy resort access.", ("Caribbean beaches", "Mayan heritage", "street food")),
    Destination("Lisbon", "Portugal", "LIS", "mild", 1900, True, ("food", "culture", "history", "nightlife"), "A walkable Atlantic city of tiled streets, neighborhood bakeries, and nearby coastlines.", ("Alfama", "seafood", "day trips")),
    Destination("Honolulu", "United States", "HNL", "warm", 2850, True, ("beach", "nature", "adventure", "relaxation"), "An island base for beaches, volcanic landscapes, and a deep Pacific cultural mix.", ("Waikiki", "Diamond Head", "island food")),
    Destination("Barcelona", "Spain", "BCN", "mild", 2200, True, ("food", "culture", "history", "nightlife"), "Mediterranean energy, bold architecture, long lunches, and an accessible urban beach.", ("Gaudi architecture", "tapas", "coast")),
    Destination("Reykjavik", "Iceland", "KEF", "cold", 2600, True, ("nature", "adventure", "relaxation"), "A compact Nordic capital that opens into geothermal pools, waterfalls, and northern landscapes.", ("Blue Lagoon", "waterfalls", "aurora")),
    Destination("Tokyo", "Japan", "NRT", "mild", 2450, True, ("food", "culture", "history", "nightlife"), "A high-energy city where centuries-old neighborhoods sit beside precise modern design.", ("ramen", "temples", "neighborhoods")),
    Destination("Cape Town", "South Africa", "CPT", "warm", 2050, False, ("nature", "food", "adventure", "culture"), "A dramatic coastal city framed by mountains, vineyards, and a layered culinary scene.", ("Table Mountain", "wine country", "coast")),
    Destination("Vancouver", "Canada", "YVR", "mild", 2300, True, ("nature", "food", "adventure", "relaxation"), "An easygoing Pacific city with mountain access, excellent food, and urban green space.", ("Stanley Park", "mountains", "seafood")),
]

# Deterministic synthetic catalog expansion keeps local demos representative
# without claiming these records are live inventory or booking availability.
_regions = [
    ("Valencia", "Spain", "VLC", "mild", ("food", "culture", "beach")),
    ("Marrakesh", "Morocco", "RAK", "warm", ("food", "culture", "history")),
    ("Auckland", "New Zealand", "AKL", "mild", ("nature", "adventure", "food")),
    ("San Jose", "Costa Rica", "SJO", "warm", ("nature", "adventure", "relaxation")),
    ("Edinburgh", "United Kingdom", "EDI", "cold", ("history", "culture", "food")),
    ("Athens", "Greece", "ATH", "warm", ("history", "culture", "food")),
    ("Seoul", "South Korea", "ICN", "mild", ("food", "culture", "nightlife")),
    ("Melbourne", "Australia", "MEL", "mild", ("food", "culture", "nature")),
    ("Montreal", "Canada", "YUL", "cold", ("food", "culture", "history")),
    ("Cartagena", "Colombia", "CTG", "warm", ("beach", "food", "history")),
]
_synthetic_catalog = []
for _index in range(10):
    for _city, _country, _airport, _climate, _interests in _regions:
        _synthetic_catalog.append(Destination(_city, _country, _airport, _climate, 1500 + ((_index * 137) % 1500), True, _interests, f"A curated {_climate} travel starting point in {_city} with {_interests[0]} and {_interests[1]}.", (f"{_city} neighborhoods", _interests[0], _interests[1])))
DESTINATIONS = DESTINATIONS + _synthetic_catalog
