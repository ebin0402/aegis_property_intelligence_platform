def investment_score(property_data):
    price = property_data.get("price", 0)
    rent_estimate = property_data.get("rent_estimate", price * 0.005)

    yield_percent = (rent_estimate * 12) / price * 100

    risk = 100 - yield_percent

    return {
        "yield": round(yield_percent, 2),
        "risk": round(max(0, min(100, risk)), 2),
        "recommendation": "Good" if yield_percent > 5 else "Weak"
    }
