import json
from collections import defaultdict
from datetime import datetime

def load_inventory(path="sponsorship_inventory.json"):
    with open(path, "r") as f:
        return json.load(f)

def load_ledger(path="sponsorship_ledger.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_ledger(ledger, path="sponsorship_ledger.json"):
    with open(path, "w") as f:
        json.dump(ledger, f, indent=2)

def suggest_package(budget, tier="Gold", preferred_duration=12):
    inventory = load_inventory()
    ledger = load_ledger()
    used_slots = defaultdict(int)
    for asset, entries in ledger.items():
        used_slots[asset] = len(entries)

    package = []
    total_cost = 0
    total_impressions = 0

    tier_weight = {
        "Exclusive Naming": 3.0,
        "Presenting": 2.0,
        "Gold": 1.5,
        "Silver": 1.2,
        "Bronze": 1.0
    }

    base_costs = {
        "Dome Naming Rights": 50000,
        "Field Naming Rights": 30000,
        "Scoreboard Ad Panel": 10000,
        "Website Banner": 5000,
        "Email Footer": 2000,
        "Social Media Series Sponsor": 12000,
        "Concession Stand Signage": 3500,
        "Stadium Wall Banner": 4000,
        "Bench Sponsor": 2000,
        "Golf Cart Branding": 3000,
        "Trailhead Signage": 2500,
        "Batting Cage Naming": 7500,
        "Team Suite Sponsor": 5000,
        "Workout Facility Sponsor": 9000,
        "Lobby Wall Banner": 4000,
        "Mobile App Banner Ad": 2500,
        "Coach Shirt Sponsor": 1500,
        "Event Tent Branding": 1800,
        "Walking Trail Signs": 1000,
        "Tournament Program Full Page Ad": 3500,
        "Esports Suite Naming": 8500
    }

    for asset, config in inventory.items():
        if asset not in base_costs:
            continue

        remaining = config["max"] - used_slots.get(asset, 0)
        if remaining <= 0:
            continue

        multiplier = tier_weight.get(tier, 1.0)
        duration_factor = 1 + (preferred_duration / 12 * 0.3)
        cost = base_costs[asset] * multiplier * duration_factor

        if total_cost + cost > budget:
            continue

        package.append({
            "Asset": asset,
            "Tier": tier,
            "Duration": preferred_duration,
            "Suggested Cost": round(cost, 2),
            "Estimated Impressions": config["impressions"],
            "Remaining Slots": remaining
        })

        total_cost += cost
        total_impressions += config["impressions"]

    return {
        "Recommended Package": package,
        "Total Cost": round(total_cost, 2),
        "Estimated Impressions": total_impressions,
        "Note": "AI-generated optimal bundle based on current availability and pricing." if package else "No valid package found for this budget."
    }

def claim_package(package, sponsor_name="TBD"):
    ledger = load_ledger()
    timestamp = datetime.utcnow().isoformat()
    for item in package:
        entry = {
            "sponsor": sponsor_name,
            "timestamp": timestamp,
            "tier": item["Tier"],
            "duration": item["Duration"],
            "price": item["Suggested Cost"]
        }
        ledger.setdefault(item["Asset"], []).append(entry)
    save_ledger(ledger)
