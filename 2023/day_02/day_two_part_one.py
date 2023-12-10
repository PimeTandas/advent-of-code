file = open("day_02_input.txt", 'r')
answer = 0

for line in file.readlines():
    flag = True
    ID, line = line.split(':')
    for event in line.split(';'):
        for test in event.split(','):
            n, color = test.split()
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                flag = False
    if flag:
        print(ID)
        answer += int(ID.split()[1])
print(answer)