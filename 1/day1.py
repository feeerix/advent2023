from typing import List

letter_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "fourty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
        }

def read_file(filepath:str) -> str:
    contents = ""
    with open(filepath, "r") as file:
        contents = file.read()

    return contents

def is_number(character:str):
    if len(character) == 1:
        return character.isdigit()
    return False

def get_numbers(input_str:str) -> List[int]:
    parse_data = list(input_str)
    output_data = []
    for char in parse_data:
        if is_number(char):
            output_data.append(char)

    return output_data

    #print(input_str)
    #return [int(num) for num in re.findall(r'\d+', str(input_str))]


def calibrate(input_value):
    parse_data = input_value.split("\n")
    values = 0
    for line in parse_data:
        for option in letter_mapping.keys():
            
            if option in line:
                line = line.replace(option, str(letter_mapping[option]))

        numbers = get_numbers(line)
        if numbers:
            values += int(str(numbers[0])+str(numbers[-1]))
    
    print(values)

file_data = read_file("input.txt")
calibrate(file_data)
