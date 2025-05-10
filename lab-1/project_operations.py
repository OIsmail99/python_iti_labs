import json


def viewAllProjects():
    with open("projects.json", 'r') as projectsFile:
        projects = json.loads(projectsFile.read())
        i = 0
        for project in projects:
            i = i + 1
            print("------------------------------------------------")
            print(f"project number: {i}")
            print(f"Title: {project['title']}, Description: {project['description']}, Total Target: {project['total_target']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")



def addProject(user_id:int, title:str, description:str, total_target:int, start_date:str, end_date:str):
    # Code to add a new project to the projects.json file
    newProject = {"user_id": user_id ,"title": title, "description": description, "total_target": total_target, "start_date": start_date, "end_date": end_date}
    with open("projects.json", 'r+') as projectsFile:
        projects = json.loads(projectsFile.read())
        projects.append(newProject)
        projectsFile.seek(0)
        projectsFile.write(json.dumps(projects))
        projectsFile.truncate()