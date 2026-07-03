def search_properties(properties, filters):
    results = properties

    if "min_price" in filters:
        results = [p for p in results if p["price"] >= filters["min_price"]]

    if "max_price" in filters:
        results = [p for p in results if p["price"] <= filters["max_price"]]

    if "bedrooms" in filters:
        results = [p for p in results if p["bedrooms"] == filters["bedrooms"]]

    if "location" in filters:
        results = [p for p in results if filters["location"].lower() in p["location"].lower()]

    return results
