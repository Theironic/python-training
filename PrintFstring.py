# way to show variables

name = "jon smith"

name2 = 'ana evans'

print("here have a name -",name)

print(name, "-",name2)

name = input("your name")

print("welcome" + name + "!")

#Python has a feature that automatically break the line after print

#let's see how to disable this

print('this line will be broken automatically')
print('this line will not be automatically broken,', end='')
print(' work!')

# now you will see python .format

name3 = 'joe'

age = 47
msg = "welcome {0} your age is {1}".format(name3,age)

print (msg)

# Now you will see what I use most, fstring
print(f'testinf f string {name} and {name2}')

# fstring with numbers
x = 10
y = 20
print(f'x + y = {x + y}')