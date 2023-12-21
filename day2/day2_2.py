with open('day2_1.txt', 'r') as file:
    lines = [line.strip().split(":") for line in file]
    
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

