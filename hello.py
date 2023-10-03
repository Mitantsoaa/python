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
print(x+z)
print(x-z)
print(x*z)
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

