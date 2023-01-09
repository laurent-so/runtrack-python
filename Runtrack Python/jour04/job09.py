L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

minimum = L[0]
maximum = L[0]

for element in L:
    if element < minimum:
        minimum = element
    if element > maximum:
        maximum = element

print("Minimum:", minimum)
print("Maximum:", maximum)
