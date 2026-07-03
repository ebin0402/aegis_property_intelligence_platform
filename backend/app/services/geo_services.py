import math

def distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def filter_by_radius(properties, center, radius):
    results = []

    for p in properties:
        if "lat" not in p:
            continue

        d = distance(center["lat"], center["lng"], p["lat"], p["lng"])
        if d <= radius:
            results.append(p)

    return results
