def chiffrement_cesar(message, decalage):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  message_chiffre = ""
  for lettre in message:
    if lettre.lower() in alphabet:
      lettre_chiffree = alphabet[(alphabet.index(lettre.lower()) + decalage) % 26]
      if lettre.isupper():
        message_chiffre += lettre_chiffree.upper()
      else:
        message_chiffre += lettre_chiffree
    else:
      message_chiffre += lettre
  return message_chiffre

message = "Je suis le danger"
decalage = 5
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)
