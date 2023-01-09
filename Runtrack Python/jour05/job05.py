def distance_parcourue(marches, hauteur_marche):
  ascenseurs = 5 * 2  
  distance = ascenseurs * marches * hauteur_marche / 100  
  distance_semaine = distance * 7  
  return distance_semaine

marches = 10
hauteur_marche = 20
distance_semaine = distance_parcourue(marches, hauteur_marche)
print(f"Pour {marches} marches de {hauteur_marche} cm, le gardien parcours {distance_semaine:.2f} m par semaine.")
