def check_type_saison(type, saison):
  if type == "fruits" and saison == "hiver":
    print("orange, mandarine et kiwi")
  elif type == "fruits" and saison == "été":
    print("poire, fraise, cassis")
  elif type == "légume" and saison == "hiver":
    print("carotte, topinambour, endive")
  elif type == "légume" and saison == "été":
    print("artichaut, aubergine, navet")

check_type_saison("fruits", "hiver")
check_type_saison("fruits", "été")
check_type_saison("légume", "hiver")
check_type_saison("légume", "été")

