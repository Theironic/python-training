# Now let's play a little with the Python library
import random

val = random.randint(0,10) # choose a random number between 0-10

print(val)
#############

print('write fives numbers int')

for i in range(1,6,1):
    print(f'your num is here! {random.randint(0,10)} \n')
    # you can also do the same code with this variable

print('here ! \n')

for i in range(1,4,1):
    n = random.randint(0,50)
    print(f'another example {n} \n')

# how to generate float value

z = random.random()
print('number: {0}'.format(z)) 
print(f'float number {round(z * 10, 2)} \n')

# another way
x = random.uniform(1,400)
print(f'look {x} \n')

# choose a random number
L = [1,2,3,4,5,6,7,8,9,10]
giveaway = random.choice(L)
print(f'random choice {giveaway}')
