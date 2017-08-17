import median

input = []

with open('Median.txt') as file:
    for num in file:
        input.append(int(num))

output = median.Median(input).sum_mod(10000)

print(output)




