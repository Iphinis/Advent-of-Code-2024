import os
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as file:
    lines = [list(map(int, x.strip().split())) for x in file.readlines()]

l1, l2 = zip(*lines)

l1, l2 = sorted(l1), sorted(l2)

def distance(l1, l2):
    return sum(abs(e1 - e2) for e1, e2 in zip(l1,l2))

print("Distance:", distance(l1,l2))

def similarity(l1, l2):
    counter = Counter(l2)
    
    return sum(e1 * counter[e1] for e1 in l1)

print("Similarity:", similarity(l1,l2))
