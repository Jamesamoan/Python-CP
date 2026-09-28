num = int(input("Enter a number"))
num1 = int(input("Enter a number"))
choice= input("Chose how you are going to calculate")
print("add")
print("subtract")
print("multipy")
print("divide")


def add(num,num1):
    add = num+num1
    return

print("The Sum is:",add )

def subtract(num,num1):
    subtract = num - num1
    return

print("The diffrent is:",subtract)

def multipy(num,num1):
    multipy = num*num1
    return

print("The multipication is:",multipy)

def divide(num,num1):
    divide=num/num
    return

print("The division is:",divide)

try:
    pass
except ValueError:
    print("This a value error")
except ZeroDivisionError:
    print("This a zero division")