f = open("input/12.txt", "r")
lines = f.readlines()


# part 1
compass = {}
compass[0] = 'N'
compass[90] = 'E'
compass[180] = 'S'
compass[270] = 'W'

north = 0
east = 0
direction = 'E'
degrees = 90
for line in lines:
  line = line.strip()
  instruction = line[0]
  val = int(line[1:])

  if instruction == 'F':
    instruction = direction

  if instruction == 'N':
    north += val
  elif instruction == 'S':
    north -= val
  elif instruction == 'E':
    east += val
  elif instruction == 'W':
    east -= val
  elif instruction == 'L':
    degrees = (degrees - val) % 360
    direction = compass[degrees]
  elif instruction == 'R':
    degrees = (degrees + val) % 360
    direction = compass[degrees]

print(abs(north) + abs(east))

# part 2
waypoint_north = 1
waypoint_east = 10
north = 0
east = 0
for line in lines:
  line = line.strip()
  instruction = line[0]
  val = int(line[1:])

  if instruction == 'F':
    north += waypoint_north * val
    east += waypoint_east * val
  elif instruction == 'N':
    waypoint_north += val
  elif instruction == 'S':
    waypoint_north -= val
  elif instruction == 'E':
    waypoint_east += val
  elif instruction == 'W':
    waypoint_east -= val
  elif instruction == 'L' or instruction == 'R':
    if instruction == 'L':
      val = -val % 360

    if val == 90:
      waypoint_north, waypoint_east = -waypoint_east, waypoint_north
    elif val == 180:
      waypoint_north, waypoint_east = -waypoint_north, -waypoint_east
    elif val == 270:
      waypoint_north, waypoint_east = waypoint_east, -waypoint_north

print(abs(north) + abs(east))
