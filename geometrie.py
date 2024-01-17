#EXERCICE2

# le nom du module geometrie.py

#question 1. declaration de la classe

import math

class Point:
    def __init__(self, x, y):
        self.abs = x
        self.ord = y

# question 2

    def afficher_coordonnees(self):
        print("les Coordonnées d'un point : ({}, {})".format(self.abs, self.ord))


#question 3

# Créer deux objets de type Point
point1 = Point(2, 3)
point2 = Point(5, 7)

# Afficher les coordonnées des deux points
print("Coordonnées du premier point:")
point1.afficher_coordonnees()

print("\nCoordonnées du deuxième point:")
point2.afficher_coordonnees()

#question 4

@staticmethod
def longueur(point1, point2):
        return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

#question 5

@staticmethod
def estCarre(point1, point2, point3, point4):
        distances = [
            Point.longueur(point1, point2),
            Point.longueur(point1, point3),
            Point.longueur(point1, point4),
            Point.longueur(point2, point3),
            Point.longueur(point2, point4),
            Point.longueur(point3, point4)
        ]

        # Vérifier si les longueurs des côtés sont égales (carré)
        return len(set(distances)) == 2 and 2 in [distances.count(d) for d in set(distances)]
#question 6

@staticmethod
def sontAlignes(point1, point2, point3):
        # Vérifier si les pentes des segments sont égales
        return (point2.y - point1.y) * (point3.x - point2.x) == (point3.y - point2.y) * (point2.x - point1.x)

#question 7

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def afficher_coordonnees(self):
        print("Coordonnées du point : ({}, {}, {})".format(self.x, self.y, self.z))


'''# Exemple d'utilisation dans un script Python
if __name__ == "__main__":
    # Créer deux objets de type Point
    point1 = Point(0, 0)
    point2 = Point(1, 1)

    # Afficher les coordonnées
    point1.afficher_coordonnees()
    point2.afficher_coordonnees()

    # Calculer la longueur entre les deux points
    distance = Point.longueur(point1, point2)
    print("Longueur entre les deux points : {:.2f}".format(distance))

    # Créer quatre points pour tester si ils forment un carré
    point3 = Point(0, 1)
    point4 = Point(1, 0)

    if Point.estCarre(point1, point2, point3, point4):
        print("Les quatre points forment un carré.")
    else:
        print("Les quatre points ne forment pas un carré.")

    # Créer trois points pour tester s'ils sont alignés
    point5 = Point(2, 2)
    point6 = Point(3, 3)

    if Point.sontAlignes(point1, point2, point5):
        print("Les trois points sont alignés.")
    else:
        print("Les trois points ne sont pas alignés.")

    # Créer deux objets de type Point3D
    point3D1 = Point3D(1, 2, 3)
    point3D2 = Point3D(4, 5, 6)

    # Afficher les coordonnées en 3D
    point3D1.afficher_coordonnees()
    point3D2.afficher_coordonnees()'''
