f = open("input/4.txt", "r")
lines = f.read().split('\n\n')

def validate_byr(byr):
  byr_i = int(byr)
  return len(byr) == 4 and byr_i >= 1920 and byr_i <= 2002

def validate_iyr(iyr):
  iyr_i = int(iyr)
  return len(iyr) == 4 and iyr_i >= 2010 and iyr_i <= 2020

def validate_eyr(eyr):
  eyr_i = int(eyr)
  return len(eyr) == 4 and eyr_i >= 2020 and eyr_i <= 2030

def validate_hgt(hgt):
  try:
    height = int(hgt[:-2])
    units = hgt[-2:]
    if units == 'cm':
      return height >= 150 and height <= 193
    elif units == 'in':
      return height >= 59 and height <= 76
    return False
  except ValueError:
    return False

def validate_hcl(hcl):
  if hcl[0] == '#' and len(hcl) == 7:
    for c in hcl[1:]:
      if c not in '0123456789abcdef':
        return False
      return True
  return False

def validate_ecl(ecl):
  valid_colors = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }
  return ecl in valid_colors

def validate_pid(pid):
  try:
    return len(pid) == 9 and int(pid)
  except ValueError:
    return False

def validate_passport(passport):
  if required_fields.issubset(passport.keys()) and not validate_hgt(passport['hgt']):
    # print(passport['hgt'])
    pass
  return (
    required_fields.issubset(passport.keys())
    and validate_byr(passport['byr'])
    and validate_iyr(passport['iyr'])
    and validate_eyr(passport['eyr'])
    and validate_hgt(passport['hgt'])
    and validate_hcl(passport['hcl'])
    and validate_ecl(passport['ecl'])
    and validate_pid(passport['pid'])
  )


required_fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

# part 1
valid_passports = 0
for line in lines:
  passport = {}
  fields = [x for x in line.split()]
  for field in fields:
    key, value = field.split(':')
    passport[key] = value
  if required_fields.issubset(passport.keys()):
    valid_passports += 1

print(valid_passports)


# part 2
valid_passports = 0
for line in lines:
  passport = {}
  fields = [x for x in line.split()]
  for field in fields:
    key, value = field.split(':')
    passport[key] = value
  if validate_passport(passport):
    valid_passports += 1

print(valid_passports)