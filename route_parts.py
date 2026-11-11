# Collect parts for shops on the same delivery route (Hadi or Ali)

parts = [
    {"type": "screen",  "model": "A15",     "shop": "Hadi", "faulty": True},
    {"type": "battery", "model": "Note 12", "shop": "Hadi", "faulty": False},
    {"type": "flex",    "model": "A15",     "shop": "Ali",  "faulty": True},
    {"type": "screen",  "model": "A54",     "shop": "Sami", "faulty": False},
    {"type": "battery", "model": "A15",     "shop": "Ali",  "faulty": False},
]

route_parts = []
for part in parts:
    if part["shop"] == "Hadi" or part["shop"] == "Ali":
        route_parts.append(part)

print(len(route_parts))
print(route_parts)
