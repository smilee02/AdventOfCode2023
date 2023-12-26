with open('day4.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
def string_to_arr_nums(arr):
    arr = arr.split(" ")
    arr = list(map(lambda x: int(x),list(filter(lambda x: x.isnumeric(),arr))))
    return arr

total = 0

for count, line in enumerate(lines):
    line = line.split(":")[1]
    aux = line.split("|")
    winNumbers = string_to_arr_nums(aux[0])
    myNumbers = string_to_arr_nums(aux[1])
    result = [i for i in winNumbers if i in myNumbers]
    points = pow(2,len(result)-1) if len(result) > 0 else 0
    total += points

print(total)


##############################################
###             PART TWO                   ###
##############################################

cards = [1] * len(lines)
for i, line in enumerate(lines):
    winning, yours = map(set, map(str.split, line.split(":")[1].split("|")))
    matched_count = len(winning & yours)
    print(matched_count)
    for j in range(1, matched_count + 1):
        cards[i + j] += cards[i]
    
print(sum(cards))