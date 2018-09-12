from canvasapi import Canvas
import config


canvas = Canvas(config.API_URL, config.API_KEY)

def getLocalUser():
    localUser = canvas.get_user(input("Enter the Local UserID from Canvas:"))
    print("Here is the user you selected: " + str(localUser))
    return localUser

def getHawkIDUser():
    guestHawkID = canvas.get_user(input("Enter the new Guest HawkID's UserID in Canvas:"))
    print("Here is the user you selected: " + str(guestHawkID))
    return guestHawkID


newUser = localUser.merge_into(guestHawkID)
print("You have successfully merged the accounts. The merged user is: " = str(newUser))

