# Now let's play a little with the Python library
import random

val = random.randint(0,10) # choose a random number between 0-10

print(val)
##

print('write fives numbers int')

for i in range(1,6,1):
    print(f'your num is here! {random.randint(0,10)} \n')
    # you can also do the same code with this variable

print('here ! \n')

for i in range(1,4,1):
    n = random.randint(0,50)
    print(f'another example {n} \n')