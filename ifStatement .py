# if statementes 
num1= num2 = 0.0



num1 = float(input('enter with number:'))
num2 = float(input('enter with number:'))


# if statements #check /Ifstatemenst for flowchart example
if (num1 + num2) / 2 >= 7:
    print(f"approved, yours {(num1 + num2) / 2} \n")

# if else statements

# if the average is equal to or greater than seven, write approved
if (num1 + num2) / 2 >= 7:
    print("you were approved \n")
    # you can also create var media

# otherwise, write disapproved
else:
    print("you were rejected")

average = (num1 + num2) / 2
# Python if elif else statement
if (average >= 7):
    print("good boy")
elif (average >= 5):
    print("You need to study more")
