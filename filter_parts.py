# Find all faulty parts sold to the Hadi shop
parts = [
    {"type": "screen",  "model": "A15",     "shop": "Ali",  "faulty": False},
    {"type": "battery", "model": "Note 12", "shop": "Hadi", "faulty": True},
    {"type": "flex",    "model": "A15",     "shop": "Hadi", "faulty": False},
    {"type": "screen",  "model": "A54",     "shop": "Hadi", "faulty": True},
    {"type": "battery", "model": "A15",     "shop": "Ali",  "faulty": True},
]

hadi_faulty = []
for part in parts:
    if part["shop"] == "Hadi" and part["faulty"] == True:
        hadi_faulty.append(part)
print(len(hadi_faulty)) 
print(hadi_faulty)
