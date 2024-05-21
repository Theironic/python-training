# if statementes 
num1= num2 = 0.0
average = 0.0


num1 = float(input('enter with number:'))
num2 = float(input('enter with number:'))

# if the average is equal to or greater than seven, write approved
if (num1 + num2) / 2 >= 7:
    print("you were approved")
    # you can also create var media

# otherwise, write disapproved
else:
    print("you were rejected")