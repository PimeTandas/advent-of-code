file = open("day_01_input.txt", 'r')
count = 0
num = 0
total_num = 0

for line in file.readlines():
    first_num = 0
    last_num = 0

    for char in line:
        try:
            first_num = int(char)
            break
        except:
            first_num = 0

    for char in line[-1::-1]:
        try:
            last_num = int(char)
            break
        except:
            last_num = 0

    num = int(str(first_num) + str(last_num))
    total_num += num

print(total_num)