f = open("input/7.txt", "r")
lines = f.readlines()

def find_color(color, bag):
  sub_bags = bag_rules[bag]
  for sub_bag in sub_bags:
    if sub_bag[0] == color:
      return True
    if find_color(color, sub_bag[0]):
      return True
  return False

def find_num_contains(color):
  if len(bag_rules[color]) == 0:
    return 0
  sub_bags = bag_rules[color]
  count = 0
  for sub_bag in sub_bags:
    num_contained = find_num_contains(sub_bag[0])
    if num_contained:
      count += sub_bag[1] + sub_bag[1] * num_contained
    else:
      count += sub_bag[1]
  return count

bag_rules = {}
for line in lines:
  key, value = line.split(' bags contain ')
  if value[:2] == 'no':
    bag_rules[key] = []
    continue
  for val in value.split(','):
    val = val.strip()
    num = val[0]
    color, rest = val[1:].split('bag')
    color = color.strip()
    if key not in bag_rules:
      bag_rules[key] = [(color, int(num))]
    else:
      bag_rules[key].append((color, int(num)))

count = 0
for key in bag_rules:
  if key == 'shiny gold':
    continue
  if find_color('shiny gold', key):
    count += 1
print(count)




bag_rules = {}
for line in lines:
  key, value = line.split(' bags contain ')
  if value[:2] == 'no':
    bag_rules[key] = []
    continue
  for val in value.split(','):
    val = val.strip()
    num = val[0]
    color, rest = val[1:].split('bag')
    color = color.strip()
    if key not in bag_rules:
      bag_rules[key] = [(color, int(num))]
    else:
      bag_rules[key].append((color, int(num)))
print(find_num_contains('shiny gold'))