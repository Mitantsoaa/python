class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def lire(self):
    print("En lecture")

class Gazette:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def lire(self):
    print("La gazette")


livre = Livre("After", "Harding")
gazette = Gazette("Taratra", "Mpanao gazety")


for x in (livre, gazette):
  x.lire()