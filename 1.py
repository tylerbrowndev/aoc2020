from itertools import combinations

f = open("input/1.txt", "r")
lines = f.readlines()

vals = [int(x.strip()) for x in lines]

# part a
for val in vals:
  if 2020 - val in vals:
    print(val * (2020 - val))
    break

# part b
combos = combinations(vals, 3)
for combo in list(combos):
  if sum(combo) == 2020:
    print(combo[0] * combo[1] * combo[2])