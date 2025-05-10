# import json

# with open("registeredUsers.json", "r+") as f:
#     data = json.load(f)
#     data.append({"name": "ismail"})
#     f.seek(0)
#     f.write(json.dumps(data, indent=2))
#     f.truncate()




#dicts of users(user's info + their own projects)
import json
import project_operations
import user_validations
import user_operations
from datetime import datetime
     
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

    user_operations.addUser(firstName, lastName, email, password, phone)
    mainMenu()


def loginMenu():
    isValidEmail = False
    while(not isValidEmail):
        try:
            email = input("Please Enter Email: ")
            if(user_validations.isExistingEmail(email)):
                isValidEmail = True
            else:
                raise ValueError("Email Not Found")
        except ValueError as e:
            print(e)
    
    
    isValidPassword = False
    while(not isValidPassword):
        try:
            password = input("Please Enter Password: ")
            if(user_validations.isExistingPassword(password)):
                isValidPassword = True
            else:
                raise ValueError("Invalid Password")
        except ValueError as e:
            print(e)

    print("Login Successful")
    user_operations.addLoggedInUser(user_operations.getUserByEmail(email))
    projectMenu()



def addProjectMenu():
    print("ADDING A NEW PROJECT")
    #title, description, total target, start date, end date
    isValidTitle = False
    title = ''
    while(not isValidTitle):
        try:
            title = input("Please Enter a Title: ")
            if(title[0].isdigit() or len(title) < 3):
                raise Exception
            isValidTitle = True
        except Exception as e:
            print("invalid title, try again")
    
    isValidDescription = False
    description = ''
    while(not isValidDescription):
        try:
            description = input("Please Enter description: ")
            if(description[0].isdigit() or len(description) < 10):
                raise Exception("description can't be less than 10 characters")
            isValidDescription = True
        except Exception as e:
            print(e)
    
    isValidTarget = False
    target = ''
    while(not isValidTarget):
        try:
            target = int(input("Please Enter Target: "))
            if(target < 1000):
                raise Exception("Target must be higher than 1000 ")
            isValidTarget = True
        except Exception as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid number (not a string or invalid input).")
            else:
                print("Error:", e)
    
    isValidDate = False
    startDate = 0
    endDate = 0
    while(not isValidDate):
        try:
            startDate = datetime.strptime(input("Enter start date (yyyy-mm-dd): "), "%Y-%m-%d").date()
            endDate = datetime.strptime(input("Enter end date (yyyy-mm-dd): "), "%Y-%m-%d").date()
            if(abs(endDate - startDate).days < 0 or startDate < datetime.now().date() or endDate < datetime.now().date() ):
                raise Exception
            isValidDate = True
        except Exception as e:
            print("invalid dates provided! please try again")
    
    project_operations.addProject(user_operations.getLoggedInUser()['id'], title, description, target, str(startDate), str(endDate))
    print("project added successfully")



    





def projectMenu():
    isValidChoice = False
    choice = 0
    while(not isValidChoice):
        try:
            print("Press:")
            print("1. View All Projects")
            print("2. Add a Project")
            print("3. Update a Project")
            print("4. Delete a Project")
            print("5. Exit")
            choice = int(input("Please Enter Your Choice: "))
            if(choice not in [1, 2, 3, 4, 5]):
                raise ValueError("Invalid Input. Please enter a number (1-5).")
            isValidChoice = True
        except ValueError as e:
            print(e)
    route("projectMenu", choice)




def mainMenu(message:str=""):
    print(message)
    isValidChoice = False
    while(not isValidChoice):
        try:
            print("Press:")
            print("1- Register")
            print("2- Login")
            choice = int(input("Please Enter Your Choice: "))
            if(choice not in [1, 2]):
                raise ValueError("Invalid Input. Please enter a number (1/2).")
            isValidChoice = True
        except ValueError as e:
            print(e)
    route("mainMenu", choice)


def route(lastPoint:str, choice:int):
    if(lastPoint == "mainMenu"):
        if(choice == 1): registerMenu()
        if(choice == 2): loginMenu()
    if(lastPoint == "projectMenu"):
        if(choice == 1): project_operations.viewAllProjects()
        if(choice == 2): addProjectMenu()
        # if(choice == 3): project_operations.updateProject()
        # if(choice == 4): project_operations.deleteProject()
        if(choice == 5): user_operations.mainMenu("Exiting...")
    
        

mainMenu()