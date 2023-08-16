from redminelib import Redmine
from datetime import timezone

def getRedmine(config_ini):
    
    redmine = Redmine(config_ini['Redmine']['URL'], key=config_ini['Redmine']['API'])

    return redmine

def getRedmineProject(redmine, projectName):
    
    project = redmine.project.get(projectName)

    return project