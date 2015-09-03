#Returns the sum of num1 and num2
def add(num1, num2):
    return num1+num2
#*, -, /

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1, num2):
    return num1*num2

def main():
    operation = input("What do you want to do? (+, -, *, /)")
    if(operation != '+' and operation != '-' and operation!= '*' and operation != '/'):
        #invalid operation
        print("Come again?")
    else:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        if(operation == '+'):
            print(add(num1, num2))
        if(operation == '-'):
            print(subtract(num1, num2))
        if(operation == '*'):
            print(multiply(num1, num2))
        if(operation == '/'):
            print(divide(num1, num2))
main()
        




