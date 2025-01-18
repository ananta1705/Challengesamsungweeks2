data = [
    {'nama': 'Budi', 'gaji': 5000},
    {'nama': 'Dwi', 'gaji': 8000},
    {'nama': 'Joko', 'gaji': 6000}
]

output = {
    "highest_salary": max(data, key=lambda x: x['gaji'])['nama'],
    "total_salary": sum(x['gaji'] for x in data)
}

print(output)