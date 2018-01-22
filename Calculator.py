def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
def exponent(x, y):
    return x**y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponential")
# Take input from the user
choice = input("Enter choice(1/2/3/4/5):")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice =='1':
    print(add(x, y))
elif choice =='2':
    print(subtract(x, y))
elif choice =='3':
    print(multiply(x, y))
elif choice=='4':
    print(divide(x, y))
elif choice== '5':
    print(exponent(x, y))
else:
    print('invalid input')
