import pandas as pd

market_avg = {
    "Dome Naming Rights": 50000,
    "Field Naming Rights": 30000,
    "Scoreboard Banner": 7500,
    "Website Banner": 5000,
    "Email Footer": 1500,
    "Social Media Post": 1200,
    "Concession Sign": 2000,
    "Stadium Banner": 4500,
    "Fence Banner": 3500,
    "Lobby Wall Banner": 6000
}

def calculate_sponsorship_price(asset_type, location, base_value, impressions, exclusivity_level, duration_months, tier="Standard"):
    tier_multiplier = {
        "Bronze": 1.0,
        "Silver": 1.2,
        "Gold": 1.5,
        "Presenting": 2.0,
        "Exclusive Naming": 3.0,
        "Standard": 1.1
    }

    if impressions >= 1000000:
        impression_factor = 1.5
    elif impressions >= 250000:
        impression_factor = 1.25
    elif impressions >= 100000:
        impression_factor = 1.1
    else:
        impression_factor = 1.0

    exclusivity_factor = 1.0 + (exclusivity_level * 0.2)
    duration_factor = 1 + (duration_months / 12 * 0.3)
    multiplier = tier_multiplier.get(tier, 1.1)

    adjusted_price = base_value * multiplier * impression_factor * exclusivity_factor * duration_factor

    market_price = market_avg.get(asset_type, base_value)
    difference = adjusted_price - market_price
    comparison = round((adjusted_price - market_price) / market_price * 100, 1)

    recommendation = "Accept"
    if adjusted_price < base_value * 0.9:
        recommendation = "Reject – Too Low"
    elif adjusted_price < base_value:
        recommendation = "Revise – Under Market"
    elif adjusted_price > base_value * 4.0:
        recommendation = "Revise – Too High"
    elif exclusivity_level >= 4 and tier not in ["Exclusive Naming", "Presenting"]:
        recommendation = "Revise – Tier Conflict"

    summary = {
        "Asset Type": asset_type,
        "Location": location,
        "Base Value": base_value,
        "Estimated Impressions": impressions,
        "Exclusivity Level (0–5)": exclusivity_level,
        "Duration (months)": duration_months,
        "Tier": tier,
        "Final Suggested Price": round(adjusted_price, 2),
        "Market Average": round(market_price, 2),
        "Comparison to Market": f"{comparison:+.1f}%",
        "Recommendation": recommendation
    }

    return summary
