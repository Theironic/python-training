name = "your name"; #string
num = 0; #int
dot = 0.0 #float
name2, age = "your name", 0 #string and int
real = True # boolean value

print(name);
print(dot, num,name2 )

#type funcion
print(type(dot)) # output will be float
print(type(name))# output will be string
print(type(age)) # output will be int
print(type(real)) # output will be boolean(true or false)
print(type(1+4j)) # output will be complex

#isinstance funcion
x = 50
y = 'b'
print(isinstance(x, float)) # if x == float will return true
print(isinstance(x, int)) # if x == int will return true 
print(isinstance(y, str)) # if x == string will return true 
print(isinstance(x,(int,float))) # test if x == float or int
