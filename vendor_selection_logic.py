def get_best_vendor_for_laptop(model):
    vendors = {
        "Dell Latitude 5430": [
            {"name": "Dell Official", "price": 75000, "days": 5, "rating": 5},
            {"name": "Local Vendor A", "price": 73000, "days": 7, "rating": 3}
        ]
    }
    best = min(vendors[model], key=lambda x: x['price'])
    return best

print(get_best_vendor_for_laptop("Dell Latitude 5430"))