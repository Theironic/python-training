# repeat loops
num = 1


#while
while (num <= 50):
    print(num)
    num += + 3
    
print("program is over")


num2 = 100

while (num2 >= 50):
    print(num2)
    num2 += - 3
    

#while true is similar to a menu, it stays in an infinite loop until it is finished with break

while True:
    print("Type 1 to continue and 2 to exit")
    try:
        decision = int(input(": "))
    except:
        print('data error')

    if decision == 1:
        print("let's continue")
        continue
    elif decision == 2:
        print('finished program')
        break

