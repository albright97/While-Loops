#while loops

#while loops are used to repeat a block of code an unknown number of times until a condition is met

c = 0
while c < 5:
  c = c + 1
  print(c)

#control statements
#break - used to terminate the loop entirely
#continue - skips to the next iteration of the loop
#pass - does nothing, acts as a placeholder

c = 0
while c < 5:
  c = c + 1
  if c == 3:
    break
  print(c)

c = 15
while c < 20:
  c = c + 1
  if c == 18:
    continue
print(c)