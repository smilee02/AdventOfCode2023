with open('day3_1.txt', 'r') as file:
    lines = file.readlines()

import re


def find_special_symbol_position(input_string):
    match = re.search(r'[^a-zA-Z0-9.]', input_string)
    if match:
        return match.start()
    else:
        return -1  # Return -1 if no special symbol is found



for i in range(1,len(lines)):
    