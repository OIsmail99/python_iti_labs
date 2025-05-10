import json

def projectMenu():
    print("1. View Projects")
    print("2. Add Project")
    print("3. Update Project")
    print("4. Delete Project")
    print("5. Exit")


def addProject(title:str, description:str, total_target:int, start_date:str, end_date:str):
    # Code to add a new project to the projects.json file
    newProject = {"title": title, "description": description, "total_target": total_target, "start_date": start_date, "end_date": end_date}
    with open("projects.json", 'r+') as projectsFile:
        projects = json.loads(projectsFile.read())
        projects.append(newProject)
        projectsFile.seek(0)
        projectsFile.write(json.dumps(projects))
        projectsFile.truncate()
    print("Project Added Successfully")

    pass