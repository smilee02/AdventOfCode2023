f = open('day1.txt')

total = 0

for line in f:
    num_list = list(filter(lambda x: x.isnumeric(),line))
    value = ((num_list[0]) + (num_list[-1]))
    total += int(value)
print(total)

##############################################
###             PART TWO                   ###
##############################################

total = 0

values_letters = {
        "one": "o1e", 
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"}

for line in f:
    for word in values_letters.keys():
        if word in line:
            line = line.replace(word, values_letters[word])
    num_list = list(filter(lambda x: x.isnumeric(),line))
    value = ((num_list[0]) + (num_list[-1]))
    total += int(value)
print(total)