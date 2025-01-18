# Input array
array = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
output = []
for sublist in array:
    total = 0  
    for num in sublist:
        total += num  
    output.append(total) 
print(output)