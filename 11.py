import copy

f = open("input/11.txt", "r")
lines = f.readlines()

num_cols = len(lines[0].strip()) + 2
num_rows = len(lines) + 2
padding_row = ['.'] * num_cols

seating_map = [padding_row]
for line in lines:
  seating_map.append(['.'] + [c for c in line.strip()] + ['.'])
seating_map.append(padding_row)


# part 1
def get_occupied_neighbors(current_map, row, col):
  occupied_neighbor_count = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if i != row or j != col:
        if current_map[i][j] == '#':
          occupied_neighbor_count += 1
  return occupied_neighbor_count

previous_map = None
while previous_map != seating_map:
  previous_map = copy.deepcopy(seating_map)
  for row in range(1, num_rows - 1):
    for col in range(1, num_cols - 1):
      current_space = previous_map[row][col]
      if current_space == 'L':
        if get_occupied_neighbors(previous_map, row, col) == 0:
          seating_map[row][col] = '#'

      elif current_space == '#':
        if get_occupied_neighbors(previous_map, row, col) >= 4:
          seating_map[row][col] = 'L'

print(sum([row.count('#') for row in seating_map]))

# part 2
seating_map = [padding_row]
for line in lines:
  seating_map.append(['.'] + [c for c in line.strip()] + ['.'])
seating_map.append(padding_row)


def get_occupied_visible(current_map, row, col):
  occupied_visible_count = 0

  # up
  i = row - 1
  j = col
  while i > 0 and current_map[i][j] == '.':
    i -= 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # down
  i = row + 1
  j = col
  while i < len(current_map) - 1 and current_map[i][j] == '.':
    i += 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # left
  i = row
  j = col - 1
  while j > 0 and current_map[i][j] == '.':
    j -= 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # right
  i = row
  j = col + 1
  while j < len(current_map[0]) - 1 and current_map[i][j] == '.':
    j += 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # up-left
  i = row - 1
  j = col - 1
  while i > 0 and j > 0 and current_map[i][j] == '.':
    i -= 1
    j -= 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # up-right
  i = row - 1
  j = col + 1
  while i > 0 and j < len(current_map[0]) - 1 and current_map[i][j] == '.':
    i -= 1
    j += 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  # down-left
  i = row + 1
  j = col - 1
  while i < len(current_map) - 1 and j > 0 and current_map[i][j] == '.':
    i += 1
    j -= 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1
  
  # down-right
  i = row + 1
  j = col + 1
  while i < len(current_map) - 1 and j < len(current_map[0]) - 1 and current_map[i][j] == '.':
    i += 1
    j += 1
  if current_map[i][j] == '#':
    occupied_visible_count += 1

  return occupied_visible_count


previous_map = None
while previous_map != seating_map:
  previous_map = copy.deepcopy(seating_map)
  for row in range(1, num_rows - 1):
    for col in range(1, num_cols - 1):
      current_space = previous_map[row][col]
      if current_space == 'L':
        if get_occupied_visible(previous_map, row, col) == 0:
          seating_map[row][col] = '#'

      elif current_space == '#':
        if get_occupied_visible(previous_map, row, col) >= 5:
          seating_map[row][col] = 'L'

print(sum([row.count('#') for row in seating_map]))
