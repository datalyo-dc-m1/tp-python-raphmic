# Déclaration de la classe Phone qui définit une catégorie de téléphones
class Singe :

    def __init__(self, name):
            self.name = name


    def mange(self, banane):
        print(self.name,"mange une babane de couleur", banane.couleur)

    def reproduire(self, name):
        print(self.name,"et", S2.name, "reproduisent", S3.name)


class banane :
    def __init__(self, couleur):
        self.couleur = couleur

b1= banane("jaune")
b2= banane("rouge")

S1 = Singe("pierre")
S2 = Singe("marie")
S3 = Singe("robert")
S1.reproduire(S2)