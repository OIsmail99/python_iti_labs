import json
import user_validations
#import project_operations

def getLoggedInUser()->dict:
    with open("loggedInUser.json", 'r') as loggedInUsersFile:
        read = json.loads(loggedInUsersFile.read())
        return read


def getUserByEmail(email:str):
    user = {}
    with open("registeredUsers.json", 'r') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        for i in read:
            if(i["email"] == email):
                user = i
                return user
    return user


def addUser(firstName:str, lastName:str, email:str, password:str, phone:str):
    with open("registeredUsers.json", 'r+') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        newUser = {
            "id": len(read) + 1,
            "firstName": firstName, 
            "lastName": lastName, 
            "email": email, 
            "password": password, 
            "phone": phone
            }
        read.append(newUser)
        registerdUsersFile.seek(0)  
        registerdUsersFile.write(json.dumps(read))
        registerdUsersFile.truncate()
    print("User Added Successfully")    



def addLoggedInUser(user:dict):
    LoggedInUser = user
    with open("loggedInUser.json", 'w') as loggedInUsersFile:
        loggedInUsersFile.write(json.dumps(LoggedInUser))





