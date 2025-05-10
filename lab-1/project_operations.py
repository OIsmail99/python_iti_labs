import json


def viewAllProjects():
    with open("projects.json", 'r') as projectsFile:
        projects = json.loads(projectsFile.read())
        i = 0
        for project in projects:
            i = i + 1
            print("------------------------------------------------")
            print(f"project number: {i}")
            print(f"Project ID: {project['id']}, Title: {project['title']}, Description: {project['description']}, Total Target: {project['total_target']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")


def viewUserProjects(user_id):
    with open("projects.json", 'r') as projectsFile:
        projects = json.loads(projectsFile.read())
        user_projects = filter(lambda project:project['id'] == user_id, projects)
        i = 0
        for project in user_projects:
            i = i + 1
            print("------------------------------------------------")
            print(f"project number: {i}")
            print(f"Project ID: {project['id']}, Title: {project['title']}, Description: {project['description']}, Total Target: {project['total_target']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")



def deleteUserProject(user_id:int, project_id: int):
    with open("projects.json", 'r+') as projectsFile:
        projects = json.loads(projectsFile.read())
        for project in projects:
            if(project['id'] == project_id and project['user_id'] == user_id):
                projects.remove(project)
                projectsFile.seek(0)  
                projectsFile.write(json.dumps(projects))
                projectsFile.truncate()
                return True
        
    return False




def addProject(user_id:int, title:str, description:str, total_target:int, start_date:str, end_date:str):
    # Code to add a new project to the projects.json file
    with open("projects.json", 'r+') as projectsFile:
        projects = json.loads(projectsFile.read())
        newProject = { "id": len(projects) + 1  , "user_id": user_id ,"title": title, "description": description, "total_target": total_target, "start_date": start_date, "end_date": end_date}
        projects.append(newProject)
        projectsFile.seek(0)
        projectsFile.write(json.dumps(projects))
        projectsFile.truncate()