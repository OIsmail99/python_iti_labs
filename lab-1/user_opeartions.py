import json


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






def addLoggedInUser(email:str, password:str):
    LoggedInUser = {"email": email, "password": password}
    with open("loggedInUser.json", 'w') as loggedInUsersFile:
        loggedInUsersFile.write(json.dumps(LoggedInUser))