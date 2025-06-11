# Standard deviation
# User input any amount of numbers to determine how far apart set of numbers are
import math
numbers = input("Please Enter any amount of numbers separated by spaces")

numbers = [float(z.strip()) for z in numbers.split(' ')]

sum = 0
total_num = len(numbers)

for i in numbers:
    sum = sum + i

mean = sum / total_num
print("Mean is:",int(mean))

sigma = []

for x in numbers:
    sigma.append(pow(x - mean, 2))

print("Sigma is:",sigma)

sigma_sum = 0
for y in sigma:
    sigma_sum = sigma_sum + y

sigma_sum = sigma_sum / total_num

standard_deviation = math.sqrt(sigma_sum)

print(f"Standard Deviation is: {standard_deviation:.2f}")


