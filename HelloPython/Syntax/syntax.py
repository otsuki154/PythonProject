# Khong can dinh nghia kieu bien, va co the thay doi kieu bien
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

#Variable names are case-sensitive.
a = 4
A = "Sally"
print(a)
print(A)

#multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#can assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)