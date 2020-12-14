f = open("input/14.txt", "r")
lines = f.readlines()

import re
from itertools import product

# part 1
mask = ''
mems = {}
for line in lines:
  if line[:4] == 'mask':
    mask = line[7:].strip()
  else:
    mem = int(re.search(r'\[([\d]+)\]', line).group(1))
    val = int(re.search(r'= (\d+)', line).group(1))
    val_bin = format(val, '036b')

    for i in range(len(mask)):
      if mask[i] != 'X':
        val_bin = list(val_bin)
        val_bin[i] = mask[i]
        val_bin = ''.join(val_bin)
        mems[mem] = int(val_bin, 2)

total = 0
for val in mems.values():
  if val != 0:
    total += val
print(total)


# part 2
mask = ''
mems = {}
for line in lines:
  if line[:4] == 'mask':
    mask = line[7:].strip()
  else:
    mem = int(re.search(r'\[([\d]+)\]', line).group(1))
    val = int(re.search(r'= (\d+)', line).group(1))
    mem_bin = format(mem, '036b')
    mem_bin = list(mem_bin)
    variable_indices = []

    for i in range(len(mask)):
      if mask[i] == '1':
        mem_bin[i] = mask[i]
      elif mask[i] == 'X':
        variable_indices.append(i)

    perms = product(['0', '1'], repeat=len(variable_indices))
    for p in list(perms):
      for i in range(len(variable_indices)):
        mem_bin[variable_indices[i]] = p[i]
      mems[int(''.join(mem_bin), 2)] = val

total = 0
for val in mems.values():
  if val != 0:
    total += val
print(total)