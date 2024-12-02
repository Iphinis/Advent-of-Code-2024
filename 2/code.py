import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as file:
    reports = [list(map(int, report.strip().split())) for report in file]

def isSafe(report : list) -> bool:
    diff = None
    for i in range(len(report)-1):
        current_level = report[i]
        next_level = report[i+1]

        current_diff = current_level - next_level

        if diff == None:
            diff = current_diff

        if current_diff == 0 or diff*current_diff <= 0 or abs(current_diff) > 3:
            return False
    return True

print("Safe reports:", sum(map(isSafe, reports)))

def isSafeTolerate(report : list) -> bool: 
    return isSafe(report) or any(isSafe(report[:i] + report[i+1:]) for i in range(len(report)))

print("Safe reports with at most 1 bad level:", sum(map(isSafeTolerate, reports)))