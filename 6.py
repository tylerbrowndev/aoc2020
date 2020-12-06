f = open("input/6.txt", "r")
groups = f.read().split('\n\n')

# part 1
total_affirmatives = 0
for group in groups:
  affirmatives = set()
  for line in group.split('\n'):
    for c in line:
      affirmatives.add(c)
  total_affirmatives += len(affirmatives)

print(total_affirmatives)

# part 2
total_unanimous = 0
for group in groups:
  unanimous = 0
  affirmative_freqs = {}
  lines = group.split('\n')
  num_people = len(lines)
  for line in lines:
    for c in line:
      if c not in affirmative_freqs.keys():
        affirmative_freqs[c] = 1
        if num_people == 1:
          unanimous += 1
      else:
        affirmative_freqs[c] += 1
        if affirmative_freqs[c] == num_people:
          unanimous += 1
  total_unanimous += unanimous

print(total_unanimous)