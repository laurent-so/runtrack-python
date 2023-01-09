L = [8, 24, 48, 2, 16]
nombre = 0
for i in L:
  if i % 3 == 0:
    nombre += 1
print("Nombre de multiples de 3:", nombre)