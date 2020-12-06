f = open("input/5.txt", "r")
lines = f.readlines()

# part 1
max_seat_id = 0
for line in lines:
  line = line.strip()
  row = line[:7]
  row_bin = ""
  for c in row:
    row_bin += '0' if c == 'F' else '1'
  row_pos = int(row_bin, 2)
  
  col = line[7:]
  col_bin = ""
  for c in col:
    col_bin += '0' if c == 'L' else '1'
  col_pos = int(col_bin, 2)

  seat_id = row_pos * 8 + col_pos
  if seat_id > max_seat_id:
    max_seat_id = seat_id

print(max_seat_id)



# part 2
seat_ids = set()
for line in lines:
  line = line.strip()
  row = line[:7]
  row_bin = ""
  for c in row:
    row_bin += '0' if c == 'F' else '1'
  row_pos = int(row_bin, 2)
  
  col = line[7:]
  col_bin = ""
  for c in col:
    col_bin += '0' if c == 'L' else '1'
  col_pos = int(col_bin, 2)

  seat_id = row_pos * 8 + col_pos
  seat_ids.add(seat_id)

for seat_id in list(seat_ids):
  if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
    print(seat_id + 1)
