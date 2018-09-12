from canvasapi import Canvas
import config

canvas = Canvas(API_URL, API_KEY)

# user = canvas.get_user(161540)
# print(user)

# channels = user.get_communication_channels()

# for channel in channels:
#   print(channel)

def getLocalUser():
  localUser = canvas.get_user(input("Enter the Local UserID from Canvas:"))
  print("Here is the user you selected:  " + str(localUser))

def getHawkIDUser():
  guestHawkID = canvas.get_user(input("Enter the new Guest HawkID's UserID in Canvas:"))
  print("")

