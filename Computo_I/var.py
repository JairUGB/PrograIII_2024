a = "Hello"
b = "World"
r = a+""+b
print (r)

def saludar(nombre):
    return "Hola,"+ nombre
print(saludar("Mundo"))

def square(x):
    return x **2
print(square(4))

def multiply(a,b=5):
    return a*b
print(multiply(3,2))

def is_odd(num):
    return num % 2 !=0
print(is_odd(7))

def greet(name="Mundo"):
    return "Hello, "+ name
print(greet("Alice"))

def func(x):
    return x*x
print(func())

def func(x):
    return x*2
print(func(3.5))

def multiply(a=5,):
    return a*b
print(multiply(2))

x = 10
x += "5"
print(x)

x = 7 // 3
y = 7 % 3
print(x, y)