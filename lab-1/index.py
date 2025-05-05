 #dicts of users(user's info + their own projects)
import json

dic = {"name": "ismail"}
dicJson = json.dumps(dic)
with open("registeredUsers.json", 'a') as registerdUsersFile:
    print(registerdUsersFile)
    # registerdUsersFile.write(dicJson)


def isExistingEmail(email:str)->bool:
    for i in registeredUsers:
        if(registeredUsers[i]["email"] == email):
            return True
    return False


def isExistingPhone(phone:str)->bool:
    for i in registeredUsers:
        if(registeredUsers[i]["phone"] == phone):
            return True
    return False


def registerMenu():
    isValidFirstName = False
    while(not isValidFirstName):
        firstName = input("Please Enter First Name: ")
        isValidFirstName = True
    
    isValidLastName = False
    while(not isValidLastName):
        email = input("Please Enter Last Name: ")
        isValidLastName = True

    
    isValidEmail = False
    while(not isValidEmail):
        email = input("Please Enter Email: ")
        isValidEmail = True
    
    
    isValidPassword = False
    while(not isValidPassword):
        password = input("Please Enter Password: ")
        isValidPassword = True
    
    isSamePassword = False
    while(not isSamePassword):
        confirmPassword = input("Please Enter Password Again: ")
        if(password == confirmPassword):
            isSamePassword = True
    
    isValidPhone = False
    while(not isValidPhone):
        phone = input("Please Enter Phone Number: ")
        isValidPhone = True

    print("")


def addUser(firstName:str, lastName:str, email:str, password:str, phone:str):
    newUser = {"firstName": firstName, 
               "lastName": lastName, 
               "email": email, 
               "password": password, 
               "phone": phone}
    registeredUsers.append(newUser)


def route(lastPoint:str, choice:int):
    if(lastPoint == "mainMenu"):
        if(choice == 1): registerMenu()
        elif(choice == 2): loginMenu()
        else: mainMenu("invalid choice")



def mainMenu(message:str=""):
    print(message)
    print("Press:")
    print("1- Register")
    print("2- Login")
    choice = int(input())
    route("mainMenu", choice)


# mainMenu()