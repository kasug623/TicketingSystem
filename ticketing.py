import configparser
from redminelib import Redmine
from datetime import timezone

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

redmine = Redmine(config_ini['Redmine']['URL'], key=config_ini['Redmine']['API'])

project = redmine.project.get('SOC')

redmine.issue.create(
    project_id='SOC',
    subject='test',
    custom_fields=[{'id': 1, 'value': '偵察'}]
)

print(project.issues[0].subject)