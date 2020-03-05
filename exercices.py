# coding: utf-8

# Exo 1 : Définir une fonction qui prend en paramètre un entier et vérifier que ce nombre est divisible par 7 mais pas par 11
# Exo 1 + : la fonction est capable de prendre un nombre indéterminé d'entiers et de renvoyer une liste de booléens

def exo_1(number: int) -> bool:
    if (number % 7 == 0) and (number % 11 != 0):
        print("Exo 1) True for " + str(number))
        return True
    else:
        print("Exo 1) False for " + str(number))
        return False

assert exo_1(77) is False
assert exo_1(42) is True

def exo_1_plus(*numbers: int) -> [bool]:
    for num in numbers:
        if (num % 7 == 0) and (num % 11 != 0):
            continue
        else:
            print("Exo 1+) False for " + str(numbers))
            return False
    print("Exo 1+) True for " + str(numbers))
    return True

assert exo_1_plus(5,43,754,43,2) is False
assert exo_1_plus(42,420,4200) is True

# Exo 2 : Définir une fonction qui reçoit une liste d'opérations bancaires et renvoie la balance finale après toutes les opérations
# Exo 2 + : mettre un argument optionel pour indiquer la balance sur le compte avant ces opérations

def exo_2(operations: []) -> int:
    liste_depenses = []
    liste_revenus = []
    for element in operations: 
        if element[0] == "D":
            depenses = int(element[2:])
            liste_depenses.append(depenses)
            print ("Exo 2) Les dépenses sont de :", sum(liste_depenses))
        elif element[0] == "R":
            revenus = int(element[2:])
            liste_revenus.append(revenus)
            print ("Exo 2) Les revenus sont de :",sum(liste_revenus))
    print ("Exo 2) Le solde de votre compte est de :", sum(liste_revenus) - sum(liste_depenses))
    return (sum(liste_revenus) - sum(liste_depenses))

result = exo_2(["D 100", "R 200", "D 50"])
assert result == 50

def exo_2_plus(operations: [], initialBalance=0) -> int:
    liste_depenses = []
    liste_revenus = []
    for element in operations: 
        if element[0] == "D":
            depenses = int(element[2:])
            liste_depenses.append(depenses)
            print ("Exo 2+) Les dépenses sont de :", sum(liste_depenses))
        elif element[0] == "R":
            revenus = int(element[2:])
            liste_revenus.append(revenus)
            print ("Exo 2+) Les revenus sont de :",sum(liste_revenus))
    print ("Exo 2+) Le solde de votre compte est de :", initialBalance + sum(liste_revenus) - sum(liste_depenses))
    return initialBalance + sum(liste_revenus) - sum(liste_depenses)

result = exo_2_plus(["D 100", "R 200", "D 50"], 100)
result2 = exo_2_plus(["D 100", "R 200", "D 50"])
assert result == 150
assert result2 == 50

# Exo 3 : Définir une fonction qui reçoit une liste de tuples et qui renvoie une liste triée de ces tuples par points (du plus grand au plus petit)
# Tuple : ("Prénom"(str), "Points" (int), "Age" (int))

def exo_3(people: [tuple]) -> [tuple]:
    for element in people:
        trie_par_indice2 = sorted(people, key=lambda tup: tup[1])
    print ("Exo 3) Nouvelle liste triée :", trie_par_indice2)
    return trie_par_indice2

result = exo_3([("Paul", 5, 23),("Jean", 3, 24),("Nico", 7, 24),("Max", 1, 24)])
assert result == [('Max', 1, 24), ('Jean', 3, 24), ('Paul', 5, 23), ('Nico', 7, 24)]
