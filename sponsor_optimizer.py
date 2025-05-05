import json

def load_inventory(path="sponsorship_inventory.json"):
    with open(path, "r") as f:
        return json.load(f)

def suggest_package(budget, tier="Gold", preferred_duration=12):
    inventory = load_inventory()
    package = []
    used_slots = {}
    total_cost = 0
    total_impressions = 0

    priority = {
        "Exclusive Naming": 1,
        "Presenting": 2,
        "Gold": 3,
        "Silver": 4,
        "Bronze": 5
    }

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
        "Scoreboard Banner": 10000,
        "Website Banner": 5000,
        "Email Footer": 2000,
        "Social Media Post": 1200,
        "Concession Sign": 3500,
        "Stadium Banner": 4500,
        "Fence Banner": 3000,
        "Lobby Wall Banner": 5500
    }

    for asset, config in inventory.items():
        if asset not in base_costs:
            continue

        multiplier = tier_weight.get(tier, 1.0)
        duration_factor = 1 + (preferred_duration / 12 * 0.3)
        cost = base_costs[asset] * multiplier * duration_factor

        if total_cost + cost > budget:
            continue

        if used_slots.get(asset, 0) >= config["max"]:
            continue

        package.append({
            "Asset": asset,
            "Base Cost": base_costs[asset],
            "Tier": tier,
            "Duration": preferred_duration,
            "Suggested Cost": round(cost, 2),
            "Estimated Impressions": config["impressions"]
        })

        total_cost += cost
        total_impressions += config["impressions"]
        used_slots[asset] = used_slots.get(asset, 0) + 1

    return {
        "Recommended Package": package,
        "Total Cost": round(total_cost, 2),
        "Estimated Impressions": total_impressions,
        "Note": "Optimal bundle created based on budget and availability." if package else "No valid package found for this budget."
    }
