
# Fungsi untuk menentukan ganjil atau genap
def ganjil_genap(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append("genap")
        else:
            result.append("ganjil")
    return result

# Contoh input
input_numbers = [1, 2, 3, 4, 5]
output = ganjil_genap(input_numbers)

# Menampilkan output
print(output)