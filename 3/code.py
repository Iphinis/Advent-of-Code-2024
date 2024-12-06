import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "input.txt")

import re

def mul(text):
    matches = re.finditer("mul\(([0-9]{1,3}),([0-9]{1,3})\)", text)
    
    return sum([int(match.group(1))*int(match.group(2)) for match in matches])

def mul_enable(text):
    matches = re.finditer("(do\(\))|(don\'t\(\))|(mul\(([0-9]{1,3}),([0-9]{1,3})\))", text)

    s = 0
    calculate = True
    for match in matches:
        if match.group(1) == "do()":
            calculate = True
        elif match.group(2) == "don't()":
            calculate = False
        elif calculate and match.group(3):
            s += int(match.group(4))*int(match.group(5))

    return s

with open(input_path,"r") as file:
    text = file.read()
    print("Sum of multiplications:", mul(text))
    print("Sum of enabled multiplications:", mul_enable(text))
    