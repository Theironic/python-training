# list stores a sequence of values

num = [1,2,34,57,531,3,4,5,6,32,7,8,9,10]
print(num ,'\n')

num2 = [2,3,6,7,1,36,]

numlist =  num + num2 #The list were concatenation into one
print(numlist, '\n')

# you can access the value of a list through index, the first list item always starts at zero

print(numlist[0])

# but as we can see the list is disorganized, let's sort it in ascending order
print(f'{sorted(numlist)} look \n')