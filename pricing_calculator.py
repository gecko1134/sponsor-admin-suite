import pandas as pd

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

    min_price = base_value * 0.9
    max_price = base_value * 4.0

    recommendation = "Accept"
    if adjusted_price < min_price:
        recommendation = "Reject – Too Low"
    elif adjusted_price < base_value:
        recommendation = "Revise – Under Market"
    elif adjusted_price > max_price:
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
        "Recommendation": recommendation
    }

    return summary
