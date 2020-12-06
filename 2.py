f = open("input/2.txt", "r")
lines = f.readlines()

# part 1
valid_passwords = 0
for line in lines:
  policy, c, password = line.split()
  lower, upper = [int(x) for x in policy.split('-')]
  c = c[0]

  count = password.count(c)
  if count >= lower and count <= upper:
    valid_passwords += 1

print(valid_passwords)

# part 2
valid_passwords = 0
for line in lines:
  policy, c, password = line.split()
  first, second = [int(x) for x in policy.split('-')]
  c = c[0]
  if password[first - 1] == c and password[second - 1] != c:
    valid_passwords += 1
  elif password[first - 1] != c and password[second - 1] == c:
    valid_passwords +=1

print(valid_passwords)
