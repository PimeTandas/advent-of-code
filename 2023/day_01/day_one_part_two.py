file = open("day_01_input_1.txt", 'r')

numbers = []

for line in file.readlines():
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")
    digits = [x for x in line if x.isdigit()]
    numbers.append(int(digits[0] + digits[-1]))

print(sum(numbers))
