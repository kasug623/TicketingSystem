import myRedmine
import myEmail

def notificate(config_ini):

    issueIds = getRedmineIds(config_ini)

    redmine = myRedmine.getRedmine(config_ini)
    project = myRedmine.getRedmineProject(redmine, 'SOC')

    print("rrr,   ", redmine)

    for issueId in issueIds:
        ticket = redmine.issue.get(int(issueId))

        if hasSendPermit(ticket):
            to, cc, subject, body = parseTicket(ticket)
            myEmail.sendEmail(to, cc, subject, body)
            updateTicketSendState(ticket)

def getRedmineIds(config_ini):
    # web get pattern
    ids = myEmail.getRedmineIdsFromEmail(myEmail.getGmailClient3(config_ini))

    return ids

def parseTicket(ticket):
    return "a", "b", "c", "s"

def hasSendPermit(ticket):
    a = 1
    
    if ticket.tracker = 
    # print(tracker)
    exit()
    return True

def updateTicketSendState(ticket):
    print("aaaa")




