f = open("input/8.txt", "r")
lines = f.readlines()

# part 1
i = 0
acc = 0
visited = set()
while i not in visited:
  visited.add(i)
  op, val = lines[i].split()
  sign = val[0]
  val = int(val[1:].strip())
  if sign == '-':
    val *= -1
  
  if op == 'acc':
    acc += val
  elif op == 'jmp':
    i += val
    continue
  i += 1
print(acc)

# part 2
tested = set()
i = 0
bad_op = -1
while i < len(lines):
  i = 0
  acc = 0
  visited = set()
  line_changed = False
  while i not in visited and i < len(lines):
    visited.add(i)
    op, val = lines[i].split()
    sign = val[0]
    val = int(val[1:].strip())
    if sign == '-':
      val *= -1

    if i not in tested and not line_changed:
      if op == 'jmp':
        op = 'nop'
        line_changed = True
        bad_op = i
      elif op == 'nop':
        op = 'jmp'
        line_changed = True
        bad_op = i
      tested.add(i)

    if op == 'acc':
      acc += val
    elif op == 'jmp':
      i += val
      continue
    i += 1
  
print(acc)
print(bad_op)