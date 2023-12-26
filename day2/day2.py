values = {"red":12,"green":13,"blue":14}
total = 0

def game_number(str):
    return int(str.split()[1])

def verify(games):
    game_list = [game.split(",") for game in games.split(";")] #Get each game
    comparisons = [int(item.split()[0]) <= values[item.split()[1]] for game in game_list for item in game] #Check for each game if it passes
    return all(comparisons) #If all are true

with open('day2.txt', 'r') as file:
    lines = [line.strip().split(":") for line in file]

# Calculate total using list comprehension and sum
total = sum(game_number(line[0]) for line in lines if verify(line[1]))

print(total)

##############################################
###             PART TWO                   ###
##############################################

colors = ['red', 'green', 'blue']
total = 0  
    
def verify(games):
    power = 1
    game_list = [game.split(",") for game in games.split(";")] #Get each game
    for color in colors:
        filtered_list = [item for sublist in game_list for item in sublist if color in item]
        value = max(list(map(lambda x: int(x.split()[0]),filtered_list)))
        power *= value
    return power
    

for line in lines:
    power = verify(line[1])
    total += power
    
print(total)