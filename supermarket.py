data = {
    "Indomaret": {"Ayam": 30000, "Sayur": 15000, "Buah": 20000, "Ikan": 22000},
    "Alfamaret": {"Ayam": 25000, "Sayur": 12000, "Buah": 30000, "Ikan": 25000}
}
belanja = {"Ayam": 2, "Sayur": 1, "Ikan": 1}

total = sum(min(data["Indomaret"][i], data["Alfamaret"][i]) * j for i, j in belanja.items())

print(f"Total: {total}")