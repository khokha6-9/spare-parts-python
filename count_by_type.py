# Count parts by type using a dict as a counter

parts = [
    {"type": "screen",  "model": "A15",     "shop": "Hadi", "faulty": True},
    {"type": "battery", "model": "Note 12", "shop": "Ali",  "faulty": False},
    {"type": "flex",    "model": "A15",     "shop": "Hadi", "faulty": False},
    {"type": "screen",  "model": "A54",     "shop": "Sami", "faulty": False},
    {"type": "battery", "model": "A15",     "shop": "Ali",  "faulty": True},
]

counts = {}
for part in parts:
    part_type = part["type"]
    if part_type in counts:
        counts[part_type] = counts[part_type] + 1
    else:
        counts[part_type] = 1

print(counts)
