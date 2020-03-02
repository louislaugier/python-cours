string = "une string"
binary_data = b"gdspg,spdlg"
str(b"salut") # mauvais exemple
b"salut".encode("utf-8") # bon exemple
"salut" + "ca va" # mauvaise pratique
"il y a {} nuages".format(binary_data) # bonne pratique
f"Il y a {binary_data} nuages"

un_chiffre = 5
un_float = 5.2
1.0 == 1 == True

une_list = ["A", 22, 2.0]
une_list = list() # == []
une_list.append("un elem")
une_list.pop() # enlever dernier elem
une_list.extend(["1", 1])

[323] + ["Salut"]

# variable = snake_case
# class = CamelCase
# function = snake_case

un_dict = {}
un_dict["salut"] = 1.0
un_dict[MaClass()] = 1.0
un_dict[1.0] = "salut"
un_dict[True] = "oui"
autre_dict = {
    "clé1": 23,
    "clé2": 4
}
autre_dict.keys()[2]
autre_dict.values()
autre_dict.items()
del autre_dict["clé1"]

mon_set = {'1', 1} # set uniquement quand il y a des clés à ne pas confondre avec => {} = dict, utiliser set()
mon_set = set() # un set contient des éléments uniques
mon_set.add("clé")

salut = tuple("a", "b")
salut = ("a", "b")
type(salut)
list(set(salut))
sorted(list(set(salut)))
salut = ["a", "b", "c"]
list(set(salut))
salut = ("a", "b", "c")
salut[0]
len(salut)

if True:
    print("salut")
elif False:
    print("aaa")
else:
    print("bbb")
if len(salut) > 0 :
    print("salut")
if salut:
    print("a")
if bool(salut):
    print("a")
bool(salut)

for element in salut:
    print(element)
for i in range(len(salut)):
    element = salut[i]
    print(element)
for element in autre_dict:
    value = autre_dict[element]
    print(value)
for key, value, in autre_dict.items():
    print(key)
    print(value)
autre_dict.items()
for lettre in "ma_string":
    print(lettre)
"ma_string"[1:5] # Récuper du 1er au 5e non inclus
"ma_string"[:5] # Jusqu'au 4e element
"ma_string"[1:] # A partir du 2e element

i = 23
while i > 25:
    continue
    print("salut")
    i += 1
while "iterate over something":
    print("salut")
    break

def ma_fonction(a, b):
    c = a+b
    return c
ma_fonction("a", 2)
def fonction(d, e):
    return d, e
f = fonction("aaa", "bbb")
def une_fonction(a, b, c=3):
    return a, b*c
une_fonction(1,3)
def a_func(*args, **kwargs): # retourne un tuple avec en index 0 les arguments non nommés et en index 1 les arguments nommés
    return args
a_func(2, 3, 5, salut = 2, yo = 3)
def sum(*args):
    result = 0
    for element in args:
        result += element
    return result
sum(5,5)
sum(5,5,110,234,12)
def prod_or_sum(*args, **kwargs):
    if kwargs.get("sub"):
        result = 0
        for element in args:
            result -= element
    else:
        for element in args:
            result += element
        return result
def une_fonc(a,b,*,c=3):
    return a, c*b
une_fonc(2,3,4) # erreur
une_fonc(2,3,c=4) # pas d'erreur
a=2
def function(a):
    a += 1
function(a)
a = []
def fonction(a):
    a.append("salut")
fonction(a)
a
# ne jamais mettre de dict ou liste vide dans les args
# % = reste
# % % = quotient (collé)