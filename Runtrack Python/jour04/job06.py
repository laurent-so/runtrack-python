def swapFirstAndLast(l):
  if len(l) >= 2:
    first = l[0]
    last = l[-1]
    l[0] = last
    l[-1] = first

l = [1, 2, 3, 4, 5]

print("Avant:", l)

swapFirstAndLast(l)

print("Après:", l) 
