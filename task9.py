#  =============== Task 9 ==============
# Author: Gayathri
# Created Date: 20/03/2023
# References: W3 schools, StackOverflow to use dictonary
# This is a python program and the purpose is to calculate basic arithmetic operation + , - , * , /
# save the calculated equation to the input text file. I am allowing numbers - int, float
# Give options for user to display the saved equations from the text file or to calculate basic arithmetic operation
# If the text file is not available, then file not found exception is caught and handled.
# Added dictionary for operator and selction of work to be done.
# Added validation to check if user has provided correct selection for the dictionary variables.
#  ======================================

import operator

operator_error_message = "Please enter only operations like (+, -, *, /) to calculate: "
selection_error_message = "Please enter (1, 2, 3) only for the available selections: "

# Define operators you wanna use
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

# Define the selection
selections = {
    "1": "calculator",
    "2": "display",
    "3": "exit"
}

# Validates the entered values are numeric
def validate(number_to_validate):
    while(True):
        try:
            number_to_validate = float(number_to_validate)
            return number_to_validate
        except ValueError:
            number_to_validate = input("Please enter only numeric value: ")

# Validates the operator is entered as per selection
def validate_operator(operator):
    while(True):
        try:
            if(operator in operators):
                return operator
            else:
              operator = input(operator_error_message)
        except KeyError:
            operator = input(operator_error_message)

def validate_selection(selection):
    while(True):
        try:
            if(selection in selections):
                return selection
            else:
                selection = input(selection_error_message)
        except KeyError:
            selection = input(selection_error_message)

#Gets the input from user     
def get_inputs():
    number1 = validate(input("\nPlease enter first number: "))
    number2 = validate(input("\nPlease enter second number: "))
    operation = validate_operator(input("\n" + operator_error_message))
    return number1, number2, operation

# Validates the result
def validate_result():
    number1, number2, operation = get_inputs()
    while(True):
        try:
            result = operators[operation](number1,number2)                        
            equation = f"{number1} {operation} {number2} = {result}"
            return equation
        except ZeroDivisionError:
            print("You cannot divide a number by 0")
            number1, number2, operation = get_inputs()

print("--------------------------------------------------------")
print("----------------Basic Calculator------------------------")
print("--------------------------------------------------------")
# Start of the program
user_input = "1"
while(True):
    try:
        if(user_input == "1"):
            #Get the calculated value
            equation = validate_result()
            print("\nThe given equation: "+ equation)
            
            #Write into the file.With will alutomatically close the file after using it.
            with open("input.txt", "a") as myfile:
                myfile.write(f"\n{equation}")
                
            print("Equation added to the input text file")
        elif(user_input == "2"):        
                file_name = input("\nPlease enter the file name: ")
                file = open(file_name+ ".txt", "r")  
                data = file.read()
                print("------------------------------")
                print(data)
                file.close()            
        print("------------------------------")
        print("\nAvailable selection: \n"+
                "\n1. Calculator - Please enter 1 for calculation of 2 numbers and save to text file. "+
                "\n2. Display - Please enter 2 for reading all the equations from text file"+
                "\n3. Exit - Please enter 3 to end the program")
        user_input = input("\nPlease enter your selection: ")
        user_input = validate_selection(user_input)
        if(user_input == "3"):
            print("Thank you for using the calculator.")
            print("--------------------------------------------------------")
            break
    except FileNotFoundError as error:
        print(error)
    
        