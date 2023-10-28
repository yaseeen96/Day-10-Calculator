from logo import logo
from replit import clear


def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def divide(num1, num2):
  return num1 / num2

def multiply(num1, num2):
  return num1 * num2

calculation_complete = False

print(logo)
print("Welcome to the calculator App.")
num1 = int(input("Enter the first number: "))
while not calculation_complete:
  print("Operations")
  print("+")
  print("-")
  print("*")
  print("/")
  operation = input("Enter the operation: ")
  if operation != "+" or operation != "-" or operation != "*" or operation != "/":
    operation = input("Please enter a valid operation: ")
  num2 = int(input("Enter the second number: "))
  result = 0
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)

  
  
  print(f"the result is {result}")
  choice = input("Do you want to continue the operation with the result? type 'y' for yes and 'n' for no: ")
  if choice == "y":
    num1 = result
    clear()
  elif choice == "n": 
    print("Thank you for using my calculator")
    calculation_complete = True
  else:
    print("Please enter a valid choice")
    choice = input("Do you want to continue the operation with the result? type 'y' for yes and 'n' for no: ")
    
    
    
  