# import json

# with open("registeredUsers.json", "r+") as f:
#     data = json.load(f)
#     data.append({"name": "ismail"})
#     f.seek(0)
#     f.write(json.dumps(data, indent=2))
#     f.truncate()




#dicts of users(user's info + their own projects)
import json
import project_operations as po
import user_validations
import user_opeartions







def registerMenu():
    isValidFirstName = False
    while(not isValidFirstName):
        try:
            firstName = input("Please Enter First Name: ")
            user_validations.isValidName(firstName)
            isValidFirstName = True
        except ValueError as e:
            print(e)
    
    isValidLastName = False
    while(not isValidLastName):
        try:
            lastName = input("Please Enter Last Name: ")
            user_validations.isValidName(lastName)
            isValidLastName = True
        except ValueError as e:
            print(e)

    
    isValidEmail = False
    while(not isValidEmail):
        try:
            email = input("Please Enter Email: ")
            user_validations.isValidEmailFormat(email)
            isValidEmail = True
        except ValueError as e:
            print(e)
    
    
    isValidPassword = False
    while(not isValidPassword):
        try:
            password = input("Please Enter Password: ")
            user_validations.isValidPassword(password)
            isValidPassword = True
        except ValueError as e:
            print(e)
    
    isSamePassword = False
    while(not isSamePassword):
        confirmPassword = input("Please Enter Password Again: ")
        if(password == confirmPassword):
            isSamePassword = True
    
    isValidPhone = False
    while(not isValidPhone):
        try:    
            phone = input("Please Enter Phone Number: ")
            user_validations.isValidPhone(phone)
            isValidPhone = True
        except ValueError as e:
            print(e)

    user_opeartions.addUser(firstName, lastName, email, password, phone)


def loginMenu():
    isValidEmail = False
    while(not isValidEmail):
        try:
            email = input("Please Enter Email: ")
            user_validations.isExistingEmail(email)
            isValidEmail = True
        except ValueError as e:
            print(e)
    
    
    isValidPassword = False
    while(not isValidPassword):
        password = input("Please Enter Password: ")
        if(user_validations.isExistingUser(email, password)):
            isValidPassword = True

    print("Login Successful")
    user_opeartions.addLoggedInUser(email, password)
     


def route(lastPoint:str, choice:int):
    if(lastPoint == "mainMenu"):
        if(choice == 1): registerMenu()
        if(choice == 2): loginMenu()
        



def mainMenu(message:str=""):
    print(message)
    isValidChoice = False
    while(not isValidChoice):
        try:
            print("Press:")
            print("1- Register")
            print("2- Login")
            choice = int(input("Please Enter Your Choice: "))
            if(choice != 1 and choice != 2):
                raise ValueError
            isValidChoice = True
        except ValueError:
            print("Invalid Input. Please enter a number (1/2).")
    route("mainMenu", choice)


mainMenu()