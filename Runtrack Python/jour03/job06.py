string = "abcdefghijklmnopqrstuvwxyz" * 10

length = len(string)

import math
height = math.ceil(math.sqrt(length))

pyramid = []

for i in range(height):
  line = ""
  for j in range(i+1):
    line += string[i*(i+1)//2 + j]
  pyramid.append(line)

for line in pyramid:
  print(line)
