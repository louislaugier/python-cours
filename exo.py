# écrire une méthode pour déterminer si un nombre est premier (divisible par 1 ou par lui-même)
from math import *

def isprime(x):
    if type(x) == int:
        if x > 1: 
            # itérer entre 2 et x/2
            for i in range(2, x//2): 
                # si divisible par n'importe quel nombre entre 2 et x/2
                if (x % i) == 0: 
                    return False
            else: 
                return True
        else: 
            return False
    if type(x) == float:
        return False
    else:
        return "Not a number"

print(isprime(23))
print(isprime(564))
print(isprime(sqrt(18)))
print(isprime("test"))

############################ Pour jeudi soir ###################################

# Une fonction qui prend en paramètre un entier et vérifie que ce nombre est divisible par 7 mais pas par 11
# Exo 1 + : la fonction est capable de prendre un nombre indéterminé d'entiers et de renvoyer une liste de booléens

# Exo 2 : La fonction reçoit une liste d'opérations bancaires et renvoie le montant final après toutes les opérations (balance)
# Exo 2 + : mettre un argument optionel pour indiquer le montant sur le compte avant ces opérations

# Exo 3 : Une fonction qui reçoit une liste de tuples et elle renvoie une liste triée de ces tuples par points (du plus grand au plus petit)
# Tuple : ("Prénom"(str), "Points" (int), "Age" (int))