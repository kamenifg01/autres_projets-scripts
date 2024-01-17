#EXERCICE1

# Nom du fichier : guess_modules.py

#question 1

import random

def guessSecret(secret, essais):
    """
    Fonction pour deviner un nombre secret.

    Args:
    - secret (int): Le nombre à deviner.
    - essais (int): Le nombre d'essais disponibles.

    Returns:
    - bool: True si le nombre secret a été trouvé, False sinon.
    """

    while essais > 0:
        # Demander à l'utilisateur de saisir une valeur
        user_guess = int(input("Devinez le nombre secret : "))

        # Comparer la valeur de l'utilisateur avec le nombre secret
        if user_guess == secret:
            print("Félicitations ! Vous avez trouvé le nombre secret.")
            return True
        elif user_guess < secret:
            print("Le nombre secret est plus grand.")
        else:
            print("Le nombre secret est plus petit.")

        # Soustraire 1 au nombre d'essais
        essais -= 1
        print("Il vous reste {} essais.".format(essais))
        #print(f"il vous reste {'essais'}")

    # Si on arrive ici, l'utilisateur n'a pas trouvé le nombre secret
    print("Désolé, vous n'avez pas trouvé le nombre secret. Le nombre secret était {}.".format(secret))
    return False

# question 2

# Exemple d'utilisation :
if __name__ == "__main__":
    secret_number = 30  # Vous pouvez remplacer cela par n'importe quel nombre entier
    max_essais = 3   # Vous pouvez ajuster le nombre d'essais autorisés

    # Appeler la fonction guessSecret
    result = guessSecret(secret_number, max_essais)
    if result:
        print("Bien joué !")
    else:
        print(f"Meilleure chance la prochaine fois.le nomnbre secret etait {'secret_number'}")

# question 3

# Exemple d'utilisation :
if __name__ == "__main__":
    secret_number = random.randint(0, max) # un nombre secret est attribuer de façon aléatoire
    max_essais = 3   # Vous pouvez ajuster le nombre d'essais autorisés

    # Appeler la fonction guessSecret
    result = guessSecret(secret_number, max_essais)
    if result:
        print("Bien joué !")
    else:
        print(f"Meilleure chance la prochaine fois.le nomnbre secret etait {'secret_number'}")




