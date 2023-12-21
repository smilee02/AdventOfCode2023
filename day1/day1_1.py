f = open('day1_1.txt')

total = 0

for line in f:
    num_list = list(filter(lambda x: x.isnumeric(),line))
    value = ((num_list[0]) + (num_list[-1]))
    total += int(value)
print(total)