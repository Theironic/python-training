drinks = []

for i in range(5):
    drink = input('\n write your 5 favorite drinks : ')
    drinks.append(drink)
drinks.sort()

for drinkin in drinks:
    
    print(drinkin)