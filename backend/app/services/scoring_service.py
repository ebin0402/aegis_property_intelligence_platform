def calculate_deal_score(price, market_value, location_score=50):
    if market_value == 0:
        return 0

    value_gap = (market_value - price) / market_value * 100

    score = value_gap + (location_score * 0.3)

    return round(max(0, min(100, score)), 2)
