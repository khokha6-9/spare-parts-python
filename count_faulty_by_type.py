# Count faulty parts of each type using a dict
parts = [
    {"type": "screen",  "model": "A15",     "shop": "Hadi", "faulty": True},
    {"type": "battery", "model": "Note 12", "shop": "Ali",  "faulty": False},
    {"type": "screen",  "model": "A54",     "shop": "Sami", "faulty": True},
    {"type": "flex",    "model": "A15",     "shop": "Hadi", "faulty": False},
    {"type": "battery", "model": "A54",     "shop": "Ali",  "faulty": True},
    {"type": "screen",  "model": "Note 12", "shop": "Hadi", "faulty": False},
]

counts = {}
for part in parts:
    if part["faulty"]:
        part_type = part["type"]
        if part_type in counts:
            counts[part_type] = counts[part_type] + 1
        else:
            counts[part_type] = 1

print(counts)
