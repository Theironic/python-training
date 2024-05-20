age = 25
height = 1.75

result = (age >= 18) and (height >=1.75)


output = "Can you get in the car ? " + str(result) 
print(output, "\n")
# output will be True
print("test 2 \n")

age = 17
height = 1.75

result = (age >= 18) and (height >=1.75)

output = "Can you get in the car ? " + str(result)
print(output ,"\n")
# output will be Falte

# logical or

#the algorithm will check whether the door **or** windows are closed

door = "c"
window = "c"

alarm = (door == "o") or (window == "o")
output = "alarm activated ?" + str(alarm)
print(output, "\n")

#

money = False

output = "you have money ?" + str(money)
print(output, "\n")

money = False
money = not money

output = "you have money ?" + str(money)
print(output, "\n")