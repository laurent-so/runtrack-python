def calcule(num1, operator, num2):
  if operator == "+":
    resultat = num1 + num2
  elif operator == "-":
    resultat = num1 - num2
  elif operator == "*":
    resultat = num1 * num2
  elif operator == "/":
    resultat = num1 / num2
  elif operator == "%":
    resultat = num1 % num2
  else:
    resultat = "Erreur : opérateur inconnu"
  return resultat

print(calcule(650, "+", 15))
print(calcule(54, "-", 72))
print(calcule(20, "*", 20))
print(calcule(32, "/", 22))
print(calcule(15, "%", 3))
print(calcule(45, "&", 3))
