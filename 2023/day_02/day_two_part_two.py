file = open('day_02_input.txt', 'r')
total = 0
for line in file.readlines():
    c = 1
    dic = {"green": [], "blue": [], "red": []}
    id, line = line.split(':')
    for count in line.split(';'):
        for sample in count.split(','):
            n, color = sample.split()
            dic[color].append(int(n))
    for i in dic.keys():
        c *= max(dic[i])
    total += c
print(total)