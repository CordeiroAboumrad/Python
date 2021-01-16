def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def muliply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def operation(n1, n2, operator):
  if(operator == '+'):
    return add(n1, n2)
  elif(operator == '-'):
    return subtract(n1, n2)
  elif(operator == '*'):
    return muliply(n1, n2)
  elif(operator == '/'):
    return divide(n1, n2)
  else:
    print("Wrong operator. Please try again.")

continue_program = 'y'

while(continue_program == 'y'):
  n1 = float(input("Input the first number:\n"))
  n2 = float(input("Input the second number:\n"))
  operator = str(input("Input the proper operator (+, -, *, /):\n"))
  result_number = operation(n1, n2, operator)
  print(result_number)
  continue_program = input("Do you wish to proceed with another operation (y/n)?\n")

print("Thanks for using the program. Goodbye.")
