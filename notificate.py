import myRedmine
import myEmail

def notificate(config_ini):

    issueIds = myEmail.getRedmineIdsFromEmail(myEmail.getGmailClient3(config_ini))

    redmine = myRedmine.getRedmine(config_ini)
    project = myRedmine.getRedmineProject(redmine, 'SOC')

    print(redmine)

    for issueId in issueIds:
        ticket = redmine.issue.get(issueId)

        if hasSendPermit(ticket):
            myEmail.sendEmail()


def hasSendPermit(ticket):
    return True




