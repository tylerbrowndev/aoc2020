f = open("input/10.txt", "r")
lines = f.readlines()

nums = [int(x.strip()) for x in lines]

nums = sorted(nums)

# part 1
one_diffs = 1
three_diffs = 1
for i in range(len(nums) - 1):
  diff = nums[i + 1] - nums[i]
  if diff == 1:
    one_diffs += 1
  elif diff == 3:
    three_diffs += 1
print(one_diffs * three_diffs)

# part 2
nums = [0] + nums
valid_paths = {}
for num in nums:
  valid_paths[num] = []
for i in range(len(nums) - 1):
  num = nums[i]
  next_num = nums[i + 1]
  valid_paths[num].append(next_num)
  j = i + 2
  while j <= len(nums) - 1:
    next_num = nums[j]
    if next_num - num <= 3:
      valid_paths[num].append(next_num)
    else:
      break
    j += 1
print(valid_paths)

total_arrangements = {}
keys = list(valid_paths.keys())
for i in range(len(keys) - 1, -1, -1):
  paths = valid_paths[keys[i]]
  if len(paths) == 0:
    num_arrangements = 1
  else:
    num_arrangements = 0
    for adapter in paths:
      num_arrangements += total_arrangements[adapter]
  total_arrangements[keys[i]] = num_arrangements
print(total_arrangements[0])
