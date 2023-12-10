file = "day_01_input.txt"
numbers = []

for line in open(file):
    digits = [x for x in line if x.isdigit()]
    numbers.append(int(digits[0] + digits[-1]))
print(sum(numbers))