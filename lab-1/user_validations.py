import json


def isExistingEmail(email:str)->bool:
    with open("registeredUsers.json", 'r') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        for i in read:
            if(i["email"] == email):
                return True
    return False

def isExistingPhone(phone:str)->bool:
    with open("registeredUsers.json", 'r') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        for i in read:
            if(i["phone"] == phone):
                return True
    return False

def isExistingPassword(password:str)->bool:
    with open("registeredUsers.json", 'r') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        for i in read:
            if(i["password"] == password):
                return True
    return False


def isExistingUser(email:str, password:str)->bool:
    with open("registeredUsers.json", 'r') as registerdUsersFile:
        read = json.loads(registerdUsersFile.read())
        for i in read:
            if(i["email"] == email and i["password"] == password):
                return True
    return False



def isValidPassword(password:str)->bool:
    if(len(password) < 8):
        raise ValueError("Password must be at least 8 characters long")
    if(password.isalnum() == True):
        raise ValueError("Password must contain at least one special character")
    return True


def isValidPhone(phone:str)->bool:
    subPhone = phone[0:3]
    print(subPhone)
    if(subPhone != "010" and subPhone != "011" and subPhone != "012" and subPhone != "015"):
        raise ValueError("Invalid Phone Number Format")
    for i in phone:
        if(i.isdigit() == False or len(phone) != 11):
            raise ValueError("Invalid Phone Number Format")
    if(isExistingPhone(phone)):
        raise ValueError("Phone Number Already Exists")
    return True


def isValidName(name:str)->bool:
    if(name == ""):
        raise ValueError("Name cannot be empty")
    for i in name:
        if(i.isalpha() == False and i != " "):
            raise ValueError("Invalid Name Format")
    return True



def isValidEmailFormat(email:str)->bool:
    if(email == ""):
        raise ValueError("Email cannot be empty")
    for i in email:
        if(i == " "):
            raise ValueError("Invalid Email Format")
    if(email.index("@") == -1 or email.index(".") == -1):
        raise ValueError("Invalid Email Format")
    if(email.index("@") == 0 or email.index(".") == 0):
        raise ValueError("Invalid Email Format")
    if(email.count("@") != 1 or email.count(".") != 1 or email.index("@") > email.index(".")):
        raise ValueError("Invalid Email Format")
    if(isExistingEmail(email)):
        raise ValueError("Email Already Exists")

    return True

