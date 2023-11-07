print("Hello world !")

# commentaire en python
print ('affichage en python')

# declaration de variable
x = 15
print(x)

# variable string
y = 'Nom'
print(y)

# condition python
if x > 0:
    print('C\'est positif')
else:
    print('C\'est negatif')

# les conditions logiques
z = 20
print(x + z)
print(x - z)
print(x * z)
print(x/z)
# fonction python

def first_func():
    print('Hello kitty')

# boucle for
fruits = ["akondro", "paiso", "paoma", "manga"]
for fruit in fruits:
    print(fruit)

var_string = 'banane'
for lettre in var_string:
    print(lettre)

# fonction lambda python
a = lambda i:i * 5
print(a(2))

# add element in array
fruits.append('garana')
print(fruits)

# delete element
fruits.pop(0)
print(fruits)

# remove specific element
fruits.remove('manga')

# operateur logique
if x > z & x > 0:
    print('yeah')

if x > z | z > 0:
    print('yesss!')

if ~x:
    print('Tsy x')

if x^y:
    print(x^y)

# les liste sur python
monList = ['loha','tanana','tongotra','kibo',1, 'true', 'omby']
# longueur
print(len(monList))
# avec constructeur
monSecondList = list(('atody','akoho','vorona','kisoa','omby'))
print(monSecondList)


# acceder au liste
print(monList[2])
# derniere element
print(monList[-1])
# retourne la second jusqu' à 4é element
print(monList[1:3])
# retourne du début jusqu' au 4è element sans le compter
print(monList[:4])
# retourne la troisieme jusqu' à la fin
print(monList[2:])
# test
if 'omby' in monList:
    print('raha omby ialahy efa namidiko')
# change list item
fruits[2] = 'banana'

fruits[1:3] = ['fraise', 'coco']

print(fruits)

# Add list item
fruits.append('ketapotsy')
print(fruits)

fruits.insert(2,'voasary')
print(fruits)

# ralonger
autre = ['omby', 'gana', 'atody']
fruits.extend(autre)
print(fruits)

# remove list item
fruits.remove('voasary')
print(fruits)

fruits.pop(2)
print(fruits)

del fruits[0]

# sort list alphabet
fruits.sort()
print(fruits)

# desc sort
fruits.sort(reverse = True)
print(fruits)

