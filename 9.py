f = open("input/9.txt", "r")
lines = f.readlines()

nums = [int(x.strip()) for x in lines]

# part 1
i = 25
sumFound = True
while i < len(nums) and sumFound:
  num = nums[i]
  prev_nums = nums[i-25:i]
  sumFound = False
  for n in prev_nums:
    if num - n in prev_nums and num - n != n:
      sumFound = True
      break
  i += 1
print(num)

# part 2
solutionFound = False
for i in range(len(nums)):
  if solutionFound:
    break
  total = 0
  for j in range(i, len(nums)):
    total += nums[j]
    if total == num:
      print(min(nums[i:j+1]) + max(nums[i:j+1]))
      solutionFound = True
      break
    elif total > num:
      break