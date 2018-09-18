from canvasapi import Canvas
import config
import csv


canvas = Canvas(config.API_URL, config.API_KEY)

def getLocalUser(ID):
    if ID == None:
        localUser = canvas.get_user(\
            input("Enter the Local UserID from Canvas:"))
        print("Here is the user you selected: " + str(localUser))

    else:
        localUser = canvas.get_user(ID)
    return localUser

def getHawkIDUser(ID):
    if ID == None:
        guestUser = canvas.get_user(\
            input("Enter the new Guest HawkID's UserID in Canvas:"))
        print("Here is the user you selected: " + str(guestUser))

    else:
        guestUser = canvas.get_user(ID)
    return guestUser


##___________________________________________________________________________##

if (input("Would like to read from users.csv? (Y/N)  ")\
            in ["Y", "y", "yes", "Yes"]):
    with open('users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        merge_count = 0
        for row in csv_reader:
            if merge_count == 0:
                print("\n\nMerging users from users.csv...")
                merge_count += 1

            else:
                localUser = getLocalUser(row[0])
                guestUser = getHawkIDUser(row[1])
                print(f'  -> merging {localUser} into {guestUser}')
                localUser.merge_into(guestUser)
                merge_count += 1

        print(f'{merge_count-1} accounts have been merged on {config.domain}.')


else:
    more_users = True
    merge_count = 0
    while more_users:
        # localUser = getLocalUser()
        # guestUser = getHawkIDUser()

        newUser = "guestUser"

        #newUser = localUser.merge_into(guestUser)
        print("You have successfully merged the accounts."\
            "\n  -> The merged user is: " + str(newUser))

        if (input("Do you have more to merge? (Y/N)  ")\
                in ["Y", "y", "yes", "Yes"]):
            more_users = True
        else: more_users = False
        merge_count += 1
        print("")

    print(f"{merge_count} users have been merged\n\n")

