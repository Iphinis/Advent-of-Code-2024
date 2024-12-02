from collections import Counter

with open("input.txt", "r") as file:
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
