from typing import MutableMapping


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def muliply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation_dictionary = {
    '+': add,
    '-': subtract,
    '*': muliply,
    '/': divide,
}

def operation(n1, n2, operator):
  return operation_dictionary[operator](n1, n2)

new_operation = 'y'
aggregate_operation = 'y'

while(new_operation == 'y'):
    n1 = float(input("Input the first number:\n"))
    result_number = n1
    while(aggregate_operation == 'y'):
        n2 = float(input("Input the second number:\n"))
        operator = input("Input the operator (+, -, *, /):\n")
        result_number = operation(result_number, n2, operator)
        print(result_number)
        aggregate_operation = input("Do you wish to aggregate an operation to this result (y/n)?\n")
    aggregate_operation = 'y'

    new_operation = input("Do you wish to proceed with another operation (y/n)?\n")

print("Thanks for using the program. Goodbye.")
