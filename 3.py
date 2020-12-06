f = open("input/3.txt", "r")
lines = f.readlines()

forest = []
for line in lines:
  forest.append([c for c in line.strip()])

x_len = len(forest[0])
y_len = len(forest)

# part 1

trees = 0
x = 0
y = 0
while y < y_len - 1:
  x = (x + 3) % x_len
  y += 1
  if forest[y][x] == '#':
    trees += 1

print(trees)

# part 2
slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]
product = 1
for slope in slopes:
  trees = 0
  x = 0
  y = 0
  while y < y_len - 1:
    x = (x + slope[0]) % x_len
    y += slope[1]
    if forest[y][x] == '#':
      trees += 1
  print(trees)
  product *= trees
print(product)